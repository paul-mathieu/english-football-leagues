# -*- coding: UTF-8 -*-
import psycopg2 as psycopg2

from .core import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests


class Players(object):
    """

    """

    # ===============================================================
    #   Initialisation
    # ===============================================================
    def __init__(self, *args):
        self.parameters_dictionary = None
        self.URL = None
        self.choix = 0

    def set_parameters_dictionary(self, parameters_dictionary):
        """
        Set the query option dictionary
            :param parameters_dictionary: dictionary of values
            :type parameters_dictionary: dict
        """
        self.parameters_dictionary = {"API type": None, "country": None, "league": None, "end year": None, "club": None,
                                      "firstName": None, "lastName": None}
        self.fill_parameters_dictionary(parameters_dictionary)

    # ===============================================================
    #   Setters
    # ===============================================================
    def set_URL_Players(self):
        """
        Add the attribute URL
        """
        print(self.parameters_dictionary)

        if self.parameters_dictionary["country"] is not None and self.parameters_dictionary["club"] is not None:
            self.URL = BASE_URL + "/teams/" + self.parameters_dictionary["country"] + "/" + self.parameters_dictionary[
                "club"] + "/squad/"
            self.choix = 1
        if self.parameters_dictionary["firstName"] is not None and self.parameters_dictionary["lastName"] is not None:
            param = str(self.parameters_dictionary["lastName"]).replace(" ", "+")
            self.URL = BASE_URL + "/search/?q=" + param
            self.choix = 2
        print(self.URL)

    # ===============================================================
    #   Methods
    # ===============================================================
    def fill_parameters_dictionary(self, parameters_dictionary):
        """
        Fill the attribute parameters_dictionary
            :param parameters_dictionary: dictionary of query parameters
            :type parameters_dictionary: dict
        """
        for key in parameters_dictionary.keys():
                self.parameters_dictionary[key] = parameters_dictionary[key]

    def display(self):
        """
        Display some information about players
        """
        print(get_HTML(self.URL))
        print("\n\n\n" + self.URL)

    def json_players(self, parameters_dictionary):
        """
        Apply the query with parameters and return a dictionary (json)
            :param parameters_dictionary: dictionary of query parameters
            :type parameters_dictionary: dict
            :return json_data: json data
            :rtype json_data: dict
        """
        self.set_parameters_dictionary(parameters_dictionary)
        self.set_URL_Players()
        return self.processing()
        # self.display()

    # ===============================================================
    #   Core
    # ===============================================================

    def processing(self):
        """
        This function execute the processing chosen by the user in the variable parametre_dictionaty
            :return json_data: json data
            :rtype json_data: dict
        """
        # If we search a team squad. This part of the function return all players of team choose
        # This part is run if : parameters_dictionary["country"] != None and self.parameters_dictionary["club"] != None
        if self.choix == 1:

            html = urlopen(self.URL)
            html_soup = BeautifulSoup(html, 'html.parser')
            rows = html_soup.findAll("tr")
            players = []
            for row in rows:
                cells = row.findAll("td")
                # print(cells)
                # print("\n\n")
                if len(cells) == 17:
                    try:
                        players_entry = {
                            "shirtnumber": cells[0].text,
                            "name": cells[2].text,
                            "age": cells[4].text,
                            "position": cells[5].text,
                            "game-minutes": cells[6].text,
                            "appearances": cells[7].text,
                            "lineups": cells[8].text,
                            "subs-in": cells[9].text,
                            "subs-out": cells[10].text,
                            "subs-on-bench": cells[11].text,
                            "number statistic goals": cells[12].text,
                            "number statistic assists": cells[13].text,
                            "yellow - cards": cells[14].text,
                            "2nd-yellow-cards": cells[15].text,
                            "red-cards": cells[16].text
                        }
                        players.append(players_entry)
                    except:
                        pass
            return {'TeamPlayer': players}

        # ----------------------------------------------------------------------------------------------------------

        # This part of the function return all matches plays by one player
        # If we search a player
        elif self.choix == 2:
            # For search one players we use the query option of the web site
            # The query parameter is the last name of the player
            # After we look for when the first name give in parameter is the same
            html = urlopen(self.URL)
            html_soup = BeautifulSoup(html, 'html.parser')
            rows = html_soup.findAll("tr")
            del html, html_soup
            find = False
            for row in rows:
                cells = row.findAll("td")
                try:
                    if str(self.parameters_dictionary["firstName"]).upper() in str(cells[0].text).upper():
                        print("Player name is ", cells[0].text)
                        pnam = cells[0].text
                        playerUrl = BASE_URL + "/" + str(cells[0].a.get('href'))
                        find = True
                        break;
                except:
                    pass
            if not find: raise ValueError("Player name not found")

            # When the player was found, we recover the specific URL of this player
            html = urlopen(playerUrl)
            html_soup = BeautifulSoup(html, 'html.parser')
            print(playerUrl)
            numPlayerL = playerUrl.split("/")[-2]
            matchs = []

            i = 0
            while True:
                # Get method use by web site for recover all matches - We inject the player number and a page identifier
                getMeth = 'https://uk.soccerway.com/a/block_player_matches?block_id' \
                          '=page_player_1_block_player_matches_3&callback_params=%7B%22page%22%3A0%2C' \
                          '%22block_service_id%22%3A%22player_matches_block_playermatches%22%2C%22people_id%22%3A' + \
                          numPlayerL + '%2C%22type%22%3Anull%2C%22formats%22%3Anull%7D&action=changePage&params=%7B' \
                          '%22page%22%3A' + str(i) + '%7D'
                listGetMeth = getMeth.split("%")
                # print(listGetMeth)

                # recover html code
                htmlMatchs = requests.get(getMeth).json()["commands"][0]["parameters"]["content"]

                # Processing for recover all matches
                if len(str(htmlMatchs)) < 100:
                    return {'MatchPlayer': matchs}

                html_soup = BeautifulSoup(htmlMatchs, 'html.parser')
                rows = html_soup.findAll("tr")

                for row in rows:
                    cells = row.findAll("td")
                    try:
                        Match = {
                            "player": [{"PlayerID": numPlayerL,"PlayerName": pnam,}],
                            # "PlayerID": numPlayerL,
                            # "PlayerName": pnam,
                            "Date": cells[1].text,
                            "Ligue": cells[2].text,
                            "winerTeam": cells[3].text,
                            "Score": cells[4].text,
                            "loserTeam": cells[5].text,
                            "G": 0,
                            "C": 0
                        }

                        yellowAndGoal = []
                        index = 0
                        for nb in cells[6]:

                            try:
                                nbr = int(nb[-1])

                                yellowAndGoal[index - 1][1] = nbr
                            except:
                                type = nb.get("src")[-5]
                                yellowAndGoal.append([type, 1])
                            index += 1

                        Match.update(dict(yellowAndGoal))

                        # print(Match)
                        matchs.append(Match)

                    except:
                        pass
                i = i - 1
            pass
