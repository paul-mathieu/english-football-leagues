# -*- coding: UTF-8 -*-
# from . import core
from .core import *
from bs4 import BeautifulSoup
from urllib.request import urlopen
import xmltodict
import json
import pprint


class Teams(object):
    """
    utl type : https://uk.soccerway.com/national/england/league-one/20182019/regular-season/r48115/tables/
      -> https://uk.soccerway.com/national/[country]/[League]/[yearyear]/regular-season/tables
    """

    # ===============================================================
    #   Initialisation
    # ===============================================================

    def __init__(self, *args):
        self.parameters_dictionary = None
        self.URL = None
        # print('init')

    # ===============================================================
    #   Setters
    # ===============================================================

    def set_parameters_dictionary(self, parameters_dictionary):
        """
        Set the query option dictionary
            :param parameters_dictionary: dictionary of values
            :type parameters_dictionary: dict
        """
        self.parameters_dictionary = {"API type": None, "country": None, "league": None, "end year": None}
        self.fill_parameters_dictionary(parameters_dictionary)
        # print("test")

    def fill_parameters_dictionary(self, parameters_dictionary):
        for key in parameters_dictionary.keys():
            self.parameters_dictionary[key] = parameters_dictionary[key]

    def set_URL_teams(self):
        """
        Set the URL for the request
        """
        self.URL = BASE_URL + TEAMS_START_URL + \
                   "/" + self.parameters_dictionary["country"] + \
                   "/" + self.parameters_dictionary["league"] + \
                   "/" + get_year(self.parameters_dictionary) + \
                   TEAMS_END_URL
        # self.URL = "https://uk.soccerway.com/national/england/premier-league/20192020/regular-season/r53145/tables/"

    # ===============================================================
    #   Methods
    # ===============================================================

    def json_teams(self, parameters_dictionary):
        """
        Apply the query with parameters and return a dictionary (json)
            :param parameters_dictionary: dictionary of query parameters
            :type parameters_dictionary: dict
            :return json_data: json data
            :rtype json_data: dict
        """
        self.set_parameters_dictionary(parameters_dictionary)
        self.set_URL_teams()
        # self.display()
        # return BeautifulSoup(urlopen(self.URL), "html.parser").findAll("form")[2]

        # Definition of variables
        output_json = []
        keys = []
        is_first = True

        # Html extraction
        my_html = BeautifulSoup(urlopen(self.URL), "html.parser").findAll("form")
        my_html = BeautifulSoup(str(my_html[2]), "html.parser").findAll("tr")

        # Converting extraction to dictionary
        my_json = [json.dumps(xmltodict.parse(str(e))) for e in my_html]
        my_json = [json.loads(e) for e in my_json]

        # Filling the output JSON file
        for row in my_json[1:]:
            # print(row)
            json_row_temp = dict()
            json_row_temp["id"] = row["tr"]["@data-team_id"]
            json_row_temp["team-name"] = row["tr"]["td"][1]['a']["#text"]
            json_row_temp["team-link"] = row["tr"]["td"][1]['a']["@href"]
            json_row_temp["rank"] = ""
            # json_row_temp["matches-played"] =
            # json_row_temp["goal-difference"] =
            # json_row_temp["points"] =
            output_json.append(json_row_temp)

        # return my_json[0]
        return output_json

    # ===============================================================
    #   Prints and debugs
    # ===============================================================

    def display(self):
        # print(get_HTML(self.URL))

        # html = urlopen(self.URL)
        # html_soup = BeautifulSoup(html, "html.parser")
        # rows = html_soup.findAll("table")
        # my_xml = str(rows[0])
        # print("~~ my xml ~~")
        # my_xml.replace("\n", "")
        # print(my_xml)
        # print("~~ my xml 2 ~~")
        # print(json.dumps(xmltodict.parse(my_xml)))
        print("step 1")
        html = urlopen(self.URL)
        print("step 2")
        html_soup = BeautifulSoup(html, "html.parser")
        print("step 3")
        rows = html_soup.findAll("table")
        print("step 4")
        my_xml = str(rows[0])
        # print(my_xml)

        print(self.URL)

    def tests_api_teams(self):
        callback_params = {"season_id": "17429", "round_id": "53145", "outgroup": "", "competition_id": "8",
                           "new_design_callback": "1"}
        params = {"type": "competition_overunder_table"}
        url = 'https://uk.soccerway.com/a/block_competition_tables?' \
              'block_id=page_competition_1_block_competition_tables_6&' \
              'callback_params=' + str(callback_params) + '&' \
                                                          'action=changeTable&' \
                                                          'params=' + str(params)
        # for s in url:
        #     print("\"" if s == "'" else s, end="")
        print(url)

# data = [{'tr': {'@class': 'sub-head', 'th': [{'@class': 'sortasc sortdefaultasc', '@title': 'Rank', '#text': '#'},
#                                              {'@class': 'text team sortdefaultasc', '#text': 'Team'},
#                                              {'@class': 'number total mp',
#                                               'acronym': {'@title': 'Matches played', '#text': 'MP'}},
#                                              {'@class': 'number gd',
#                                               'acronym': {'@title': 'Goal difference', '#text': 'D'}},
#                                              {'@class': 'number points',
#                                               'acronym': {'@title': 'Points', '#text': 'P'}}]}}, {
#             'tr': {'@class': 'odd team_rank', '@data-team_id': '663', '@id': 'team_rank_row_663',
#                    'td': [{'@class': 'rank rank-dark-green', '#text': '1'}, {'@class': 'text team large-link', 'a': {
#                        '@href': '/teams/england/liverpool-fc/663/', '@title': 'Liverpool', '#text': 'Liverpool'}},
#                           {'@class': 'number total mp', '#text': '29'}, {'@class': 'number gd', '#text': '+45'},
#                           {'@class': 'number points', '#text': '82'}]}}, {
#             'tr': {'@class': 'even team_rank', '@data-team_id': '676', '@id': 'team_rank_row_676',
#                    'td': [{'@class': 'rank rank-dark-green', '#text': '2'}, {'@class': 'text team large-link', 'a': {
#                        '@href': '/teams/england/manchester-city-football-club/676/', '@title': 'Manchester City',
#                        '#text': 'Manchester City'}}, {'@class': 'number total mp', '#text': '28'},
#                           {'@class': 'number gd', '#text': '+37'}, {'@class': 'number points', '#text': '57'}]}}, {
#             'tr': {'@class': 'odd team_rank', '@data-team_id': '682', '@id': 'team_rank_row_682',
#                    'td': [{'@class': 'rank rank-dark-green', '#text': '3'}, {'@class': 'text team large-link', 'a': {
#                        '@href': '/teams/england/leicester-city-fc/682/', '@title': 'Leicester City',
#                        '#text': 'Leicester City'}}, {'@class': 'number total mp', '#text': '29'},
#                           {'@class': 'number gd', '#text': '+30'}, {'@class': 'number points', '#text': '53'}]}}, {
#             'tr': {'@class': 'even team_rank', '@data-team_id': '661', '@id': 'team_rank_row_661',
#                    'td': [{'@class': 'rank rank-dark-green', '#text': '4'}, {'@class': 'text team large-link', 'a': {
#                        '@href': '/teams/england/chelsea-football-club/661/', '@title': 'Chelsea', '#text': 'Chelsea'}},
#                           {'@class': 'number total mp', '#text': '29'}, {'@class': 'number gd', '#text': '+12'},
#                           {'@class': 'number points', '#text': '48'}]}}, {
#             'tr': {'@class': 'odd team_rank', '@data-team_id': '662', '@id': 'team_rank_row_662',
#                    'td': [{'@class': 'rank rank-dark-blue', '#text': '5'}, {'@class': 'text team large-link', 'a': {
#                        '@href': '/teams/england/manchester-united-fc/662/', '@title': 'Manchester United',
#                        '#text': 'Manchester United'}}, {'@class': 'number total mp', '#text': '29'},
#                           {'@class': 'number gd', '#text': '+14'}, {'@class': 'number points', '#text': '45'}]}}]
