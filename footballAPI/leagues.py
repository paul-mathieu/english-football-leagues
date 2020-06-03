# -*- coding: UTF-8 -*-
import time

from .core import *
from bs4 import BeautifulSoup
import numpy as np
import sys

class Leagues(object):

    # ===============================================================
    #   Initialisation
    # ===============================================================

    def __init__(self, *args):
        self.parameters_dictionary = None
        self.URL = None
        self.request = None

    def json_leagues(self, parameters_dictionary):
        self.set_parameters_dictionary_leagues(parameters_dictionary)
        self.set_URL_leagues()
        result = self.process()
        return result
        # data_visualization_general(self.process())
        # self.get_player_with_market_value_of_a_team("manchester united", 2019)
        # self.data_visualization_transfermarkt(self.get_player_with_market_value_of_a_team("arsenal", 2019))

    # ===============================================================
    #   Setters
    # ===============================================================

    def set_parameters_dictionary_leagues(self, parameters_dictionary):
        """
        Set the query option dictionary
        :param parameters_dictionary: dictionary of values
        :type parameters_dictionary: dict
        """
        self.parameters_dictionary = parameters_dictionary

    def set_URL_leagues(self):
        """
        Add the attribute URL
        """
        list_parameter_key = self.parameters_dictionary.keys()
        if "country" in list_parameter_key:
            if "league" in list_parameter_key:
                if ("winner" in list_parameter_key) and (self.parameters_dictionary['winner'].upper() == "TRUE")and ("end-year" in list_parameter_key):
                    self.URL = BASE_URL + LEAGUES_START_URL + \
                               "/" + self.parameters_dictionary["country"] + \
                               "/" + self.parameters_dictionary["league"] + \
                               "/archive/"
                    self.request = 1
            elif "all" in list_parameter_key and self.parameters_dictionary['all'].upper() == "TRUE":
                self.URL = BASE_URL + LEAGUES_START_URL + \
                           "/" + self.parameters_dictionary["country"] + \
                           "/"
                self.request = 2
            elif "type" in list_parameter_key and self.parameters_dictionary['type'].upper() == "TRUE":
                self.URL = BASE_URL + "/competitions/"
                self.request = 3
            elif len(list_parameter_key) == 2: # if there is only "API-type""country" in list_parameter_key
                self.URL = BASE_URL + "/competitions/"
                self.request = 4

    # ===============================================================
    #   Methods
    # ===============================================================

    def process(self):
        """
        run the right request depending on the request number stored in self.request
        """
        request = self.request
        if request == 1:
            return self.get_winner()
        elif request == 2:
            return self.get_all_leagues()
        elif request == 3:
            return self.get_leagues_with_type()
        elif request == 4:
            return self.get_leagues()

    def get_leagues(self):
        """
        return a json object of the main english football leagues
        :return json_object: data about leagues
        :rtype json_object: json
        """
        # ex of result : {'leagues in england': [{'league name ': 'Premier League'}, {'league name ':
        # 'Championship'},{'league name ': 'League Cup'}]}

        # https://int.soccerway.com/competitions/
        country = self.parameters_dictionary["country"]

        # we set a header so that the website will know we are a real user otherwise it will block the program
        html = requests.get(self.URL, headers=HEADERS)

        html_soup = BeautifulSoup(html.text, 'html.parser')
        country_soup = None
        data_set_names = "leagues in " + country
        data_set = {data_set_names: []}
        for list_element in html_soup.find_all('li', class_='expandable'):
            link = list_element.find('a')['href']
            link1 = link.split('/')
            if country in link1:
                country_soup = list_element
                break  # we stop here

        if country_soup is not None:
            area_id = country_soup['data-area_id']
            url_hidden_content = "https://int.soccerway.com/a/block_competitions_index_club_domestic?block_id" \
                                 "=page_competitions_1_block_competitions_index_club_domestic_4&callback_params=%7B" \
                                 "%22level%22:1%7D&action=expandItem&params=%7B%22area_id%22:%22" + area_id + "%22," \
                                                                                                              "%22level%22:2,%22item_key%22:%22area_id%22%7D "
            #  url_hidden_content is the url of the get method used by the website
            html_country_leagues = \
                requests.get(url_hidden_content, headers=HEADERS).json()["commands"][0]["parameters"][
                    "content"]  # convert the result into json
            country_league_soup = BeautifulSoup(html_country_leagues, 'html.parser')
            for link in country_league_soup.find_all('a'):
                data_set[data_set_names].append({'league name ': link.string})

        # create json object
        json_dump = json.dumps(data_set)
        json_object = json.loads(json_dump)
        return json_object

    # def get_team_id_in_league(self): #marche pas
    #     """
    #     return a json object of all the team ids in league
    #     :param league:
    #     :return:
    #     """
    #     url = "https://uk.soccerway.com/national/england/premier-league/20192020/regular-season/r53145/"
    #
    #     html = requests.get(url, headers=HEADERS)
    #
    #     html_soup = BeautifulSoup(html.text, 'html.parser')
    #     print(html_soup)
    #
    #     team_table = html_soup.find('table', {"id":"page_competition_1_block_competition_tables_7_block_competition_league_table_1_table"})
    # print("team table :", team_table)
    # team_rows = team_table.select("tbody > tr.team_rank ")
    # #print("team_rows:", team_rows)
    # for row in team_rows:
    #     team_id = row['data-team_id']
    #     team_name = row.find('a').text
    #     print(team_id)
    #     print(team_name)

    def get_all_leagues(
            self):  # marche la conversion json vers csv mais la colonne des sous leagues est mal representée
        # marche pas trop, j'ai l'impression y'a un cota
        """
        Return all the english football leagues, even sub leagues
        :return json_object: data about leagues
        :rtype json_object: json
        """
        delays = [7, 11, 6, 2, 9, 15]
        print(self.URL)

        # we set a header so that the website will know we are a real user otherwise it will block the program
        html = requests.get(self.URL, headers=HEADERS)
        html_soup = BeautifulSoup(html.text, 'html.parser')
        liste = html_soup.find('ul', class_='left-tree')
        data_set_name = "leagues and sub leagues"
        data_set = {data_set_name: []}
        for url in liste.find_all('li'):
            main_league = url.a.string
            if url['class'] == ['odd'] or url['class'] == ['even'] or url['class'] == ['expanded', 'odd'] or url[
                'class'] == ['expanded', 'even']:
                new_url = BASE_URL + url.a['href']
                # we do that to get the sub leagues of each current main leagues
                # which are only available if the current main leagues is selected (clicked)
                new_html = requests.get(new_url, headers=HEADERS)
                new_html_soup = BeautifulSoup(new_html.text, 'html.parser')
                data_dict = {"league_name": main_league, "sub leagues": []}
                listoflink = new_html_soup.select('ul.left-tree > li.expanded')[0].find_all('a')
                # if class = expanded, it's the current selected
                if len(listoflink) > 2:  # we start at 2 to avoid the main leagues and the year in url <a>
                    for i in range(2, len(listoflink)):
                        data_dict["sub leagues"].append(listoflink[i].string)
                data_set[data_set_name].append(data_dict)

            delay = np.random.choice(delays)  # we do that to slow down our web scraping thus the website won't guess
            # we are web scrapping
            time.sleep(delay)

        # create json object
        json_dump = json.dumps(data_set)
        json_object = json.loads(json_dump)
        return json_object

    def get_leagues_with_type(self):
        """
        Return a json object of the main english football competitions with their type (ex: Domestic league,
        Domestic cup) :return json_object: data about leagues
        :rtype json_object: json
        """
        country = self.parameters_dictionary["country"]
        # we set a header so that the website will know we are a real user otherwise it will block the program

        html = requests.get(self.URL, headers=HEADERS)

        html_soup = BeautifulSoup(html.text, 'html.parser')
        country_soup = None
        data_set_names = "leagues in " + country + " plus type"
        data_set = {data_set_names: []}
        for list_element in html_soup.find_all('li', class_='expandable'):
            link = list_element.find('a')['href']
            link1 = link.split('/')
            if country in link1:
                country_soup = list_element
                break  # we stop here

        if country_soup is not None:
            area_id = country_soup['data-area_id']
            url_hidden_content = "https://int.soccerway.com/a/block_competitions_index_club_domestic?block_id" \
                                 "=page_competitions_1_block_competitions_index_club_domestic_4&callback_params=%7B" \
                                 "%22level%22:1%7D&action=expandItem&params=%7B%22area_id%22:%22" + area_id + "%22," \
                                                                                                              "%22level%22:2,%22item_key%22:%22area_id%22%7D "
            #  url_hidden_content is the url of the get method used by the website

            html_country_leagues = \
                requests.get(url_hidden_content, headers=HEADERS).json()["commands"][0]["parameters"][
                    "content"]  # convert the result into json
            country_league_soup = BeautifulSoup(html_country_leagues, 'html.parser')
            for row in country_league_soup.find_all('div', class_="row"):
                data_set[data_set_names].append({'competition name ': row.find('a').string,
                                                 'competition type ': row.find('span', class_="type").string})

        # create json object
        json_dump = json.dumps(data_set)
        json_object = json.loads(json_dump)
        return json_object

        # avoir le gagnant d'une competition en ou de tou (les pr

    def get_winner(self):
        """
        return a json object of the winner of the competition which ended in end_year or all the winner of the
        competition through years with end_year="all"
        :return: json object
        """
        if self.parameters_dictionary['end-year'].isdigit():
            end_year = int(self.parameters_dictionary['end-year'])
        else:
            end_year = self.parameters_dictionary['end-year']

        # we set a header so that the website will know we are a real user otherwise it will block the program
        html = requests.get(self.URL, headers=HEADERS)

        html_soup = BeautifulSoup(html.text, 'html.parser')
        data_set_names = "winner of " + self.parameters_dictionary['league']
        data_set = {data_set_names: []}
        table_content = html_soup.find(id="page_competition_1_block_competition_archive_6-wrapper").find('table')
        # table which contains all the result
        if end_year != "all":  # we look for a winner for one season
            for row in table_content.find_all('tr')[1:]:  # we don't want the head of the table
                new_row = []  # new_row[0] -> season,  new_row[1] -> winner,
                for td in row.find_all('td'):
                    if td.find('a') is None:  # we do this way because sometimes we have <a> and sometime we don't,
                        # so we add content of td as a string in a list
                        element = td.string
                    else:
                        element = td.a.string
                    new_row.append(element)
                cleaned_season = (new_row[0].replace(" ", "").replace("\n", ""))  # we remove all the whitespaces
                # and line breaks
                cleaned_season_split = cleaned_season.split("/")
                if end_year == int(cleaned_season_split[1]):  # compare the end_year we provided and the end of
                    # current season if they match
                    json_row = {'season': cleaned_season, 'winner': new_row[1]}
                    data_set[data_set_names].append(json_row)
                    break  # we stop here because we've found what we were looking for

        else:  # we look for winners for all the season
            for row in table_content.find_all('tr')[1:]:  # we don't want the head of the table
                new_row = []  # new_row[0] -> season,  new_row[1] -> winner,
                for td in row.find_all('td'):
                    if td.find('a') is None:  # we do this way because sometimes we have and sometime we don't,
                        # so we add content of td as a string in a list
                        element = td.string
                    else:
                        element = td.a.string
                    new_row.append(element)
                cleaned_season = (new_row[0].replace(" ", "").replace("\n", ""))  # we remove all the whitespaces
                # and line breaks
                json_row = {'season': cleaned_season, 'winner': new_row[1]}
                data_set[data_set_names].append(json_row)

        # create json object
        json_dump = json.dumps(data_set)
        json_object = json.loads(json_dump)
        return json_object
