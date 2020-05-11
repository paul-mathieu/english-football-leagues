# -*- coding: UTF-8 -*-

from .core import *
from bs4 import BeautifulSoup
import pandas as pd
import statistics
from pathlib import Path
import os


class TransferMarkt(object):

    # ===============================================================
    #   Initialisation
    # ===============================================================

    def __init__(self, *args):
        self.parameters_dictionary = None
        self.URL = None
        self.request = None

    def json_transferMarkt(self, parameters_dictionary):
        self.set_parameters_dictionary(parameters_dictionary)
        # self.set_URL_leagues()
        # self.process()
#        data_visualization_general(self.process())
        #return self.get_player_with_market_value_of_a_team("manchester united", 2019)
        self.data_visualization_transfermarkt(self.get_player_with_market_value_of_a_team("arsenal", 2019))

    # ===============================================================
    #   Setters
    # ===============================================================

    def set_parameters_dictionary(self, parameters_dictionary):
        """
        Set the query option dictionary
        :param parameters_dictionary: dictionary of values
        :type parameters_dictionary: dict
        """
        self.parameters_dictionary = parameters_dictionary

    # ===============================================================
    #   Methods
    # ===============================================================

    def get_team_info(self, team):
        # WARNING : works only for premier league club for the moment
        # we do this way because we don't know how transfermarkt spells club name so we look for it by using the
        # search bar, and among the result we look for the one which best fits with the team we are looking for ( it
        # has to be in Premier league) NB : we can't have two teams with the same name in Premier League

        # NB: when we use the search bar, we might have different type of result like result table of manager, club,
        # players, etc. So we have to make sure we take the club result table.

        # NB: there are two manchester on Premier league, so the user has to type the whole name like manchester
        # united or manchester city

        """
        return the transferMarkt page link of a premier league team page
        :param team : string, team name
        :return dict: {"url_team_name ": ..., "team_id":...}
        """
        # return : {"url_team_name ": fc-burnley, "team_id":1132}
        url = "https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query={}&x=0&y=0".format(team)
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, '
                                 'like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

        # we set a header so that the website will know we are a real user otherwise it will block the program

        html = requests.get(url, headers=headers)
        html_soup = BeautifulSoup(html.text, 'html.parser')
        clubs = html_soup.select("div.large-12 > div.box > div.table-header")
        club = None
        result = []
        for c in clubs:
            if "Clubs" in c.text.split(" "):  # we take the table result of club
                club = c.find_next("div")  # we take the next div because it's this one which contains all the info
        for row in club.find_all("table", {"class": "inline-table"}):
            hrefs = row.find_all("a")
            # hrefs is a list of <a>, the first element is the team name and the second element (if it s exist it's the
            # team division )
            if len(hrefs) == 2:
                if hrefs[1]['title'] == "Premier League":  # check if the division is Premier league
                    result.append(hrefs)
                    # return {"url_team_name": hrefs[0]['href'].split("/")[1], "team_id": hrefs[0]['id']}
                    # we return the first team we find because in Premier league all team names are unique

        if len(result) > 1:
            # if there is several clubs in Premier league which corresponds to the name the user entered (ex:
            # "manchester", they will be "manchester city" and "manchester united", we don't which one of them the
            # user is looking for
            print("please be more specific on your research")
            return None
        elif len(result) == 1:
            return {"url_team_name": result[0][0]['href'].split("/")[1], "team_id": result[0][0]['id']}
        else:
            return None

    def get_player_with_market_value_of_a_team(self, team, season):
        """
        return a json object of player of team given with the market value of each player
        :param team: String, team name
        :param season: int, the beginning year of the season
        :return: json object
        """
        team_info = self.get_team_info(team)

        url = "https://www.transfermarkt.com/" + team_info["url_team_name"] + "/kader/verein/" + team_info[
            "team_id"] + "/plus/1/galerie/0?saison_id=" + str(season)

        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, '
                                 'like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

        # we set a header so that the website will know we are a real user otherwise it will block the program

        html = requests.get(url, headers=headers)
        html_soup = BeautifulSoup(html.text, 'html.parser')

        data_set_name = "player_market_value_of_" + team + "_in_" + str(season)
        data_set = {data_set_name: []}

        players = html_soup.find("table", {"class": "items"}).tbody
        for row in players.find_all("tr", recursive=False):  # recursive=False means we see direct children not the
            # descendants
            player_id = row.find("a", {"class": "spielprofil_tooltip"})['id']
            player_name = row.find("a", {"class": "spielprofil_tooltip"}).string
            player_contract_expires = row.find_all("td", {"class": "zentriert"}, recursive=False)[7].string
            # we have to do this way because there are others tds with class "zentriert" but with no id or anything else
            # so we use the index
            player_market_value = row.find("td", {"class": "rechts hauptlink"}).text.replace("\xa0", "")
            # we got "\xa0" code in the td so we replace by ""

            data_set[data_set_name].append({"player_id": player_id,
                                            "player_name": player_name,
                                            "player_contract_expires": player_contract_expires,
                                            "player_market_value": player_market_value})

        # create json object
        json_dump = json.dumps(data_set)
        json_object = json.loads(json_dump)
        return json_object

    # ===============================================================
    #   CSV and data visualisation
    # ===============================================================

    def data_visualization_transfermarkt(self, data):
        """
        transform the data (json object) to csv file
        :return:
        """
        key = list(data.keys())[0]  # we do this way because keys() return a dict-keys which is not subscriptable
        df = pd.DataFrame(data[key])

        # curating data
        df["player_market_value_€"] = df["player_market_value"].apply(self.without_money_unit)
        del df["player_market_value"]

        # saving data to csv in the jupyter_notebook directory
        file_name = key + ".csv"
        path_to_save = str(Path(__file__).parent.parent) + '/jupyter_notebook/'
        df.to_csv(os.path.join(path_to_save, file_name))

    def without_money_unit(self, entry):
        """
        remove the € symbol and m (for million) or k (for kilo)
        :param entry: string, player market value
        :return: float, the corresponding float of the entry
        """
        try:
            return float(entry)
        except ValueError:
            if (entry[len(entry) - 1]) == "m":
                return float(entry[1:len(entry) - 1]) * 10 ** 6
            if (entry[len(entry) - 1]) == "k":
                return float(entry[1:len(entry) - 1]) * 10 ** 3


    # def data_visualization_transfermarkt(self, data):
    #     """
    #     transform the data (json object) to csv file
    #     :return:
    #     """
    #     key = list(data.keys())[0]  # we do this way because keys() return a dict-keys which is not subscriptable
    #     df = pd.DataFrame(data[key])
    #
    #     # curating data
    #     df["player_market_value_€"] = df["player_market_value"].apply(self.without_money_unit)
    #     del df["player_market_value"]
    #
    #     file_name = key + ".csv"
    #     path_to_save = str(Path(__file__).parent.parent) + '/jupyter_notebook/'
    #     df.to_csv(path_to_save, file_name)
    #
    #     craftcans = pd.read_csv("player_market_value.csv", index_col=[0], sep=',', encoding="utf-8")
    #     #  index_col=[0] to get rid of the unnamed column
    #     print(craftcans.head(5))  # print 5 first row
    #
    #     # analysing data
    #     player_market_value_E = craftcans["player_market_value_€"]
    #     print("min : ", min(player_market_value_E))
    #     print("max : ", max(player_market_value_E))
    #     print("mean : ", statistics.mean(player_market_value_E))