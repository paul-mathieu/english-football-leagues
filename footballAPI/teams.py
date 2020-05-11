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
        self.set_url_teams()
        # print("test")

    def set_url_teams(self):
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
    #   Getters
    # ===============================================================

    def get_table_teams(self):
        my_html = BeautifulSoup(urlopen(self.URL), "html.parser").findAll("form")
        # my_html = BeautifulSoup(str(my_html[2]), "html.parser").findAll("tr")
        return my_html

    # ===============================================================
    #   Methods
    # ===============================================================

    def fill_parameters_dictionary(self, parameters_dictionary):
        """
        fill self.parameters_dictionary
            :param parameters_dictionary: dictionary of query parameters
        """
        for key in parameters_dictionary.keys():
            self.parameters_dictionary[key] = parameters_dictionary[key]

    # ===============================================================
    #   Output
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
        # return BeautifulSoup(urlopen(self.URL), "html.parser").findAll("form")[2]
        get_team_id("liverpool FC")

    # ===============================================================
    #   Prints and debugs
    # ===============================================================

    def display_teams(self):
        print("URL: ", self.URL, sep="")

        rows = self.get_table_teams()
        print(rows[0])

        # my_xml = str(rows[0])
        # print(my_xml)
        # print("my_xml: ", my_xml, sep="")

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

    def tests(self, parameters_dictionary):
        self.set_parameters_dictionary(parameters_dictionary)
        self.display_teams()


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


# https://int.soccerway.com/a/block_competitions_index_club_domestic?block_id=page_competitions_1_block_competitions_index_club_domestic_4&callback_params={"level":1}&action=expandItem&params={"area_id":"68","level":2,"item_key":"area_id"}

def get_team_id(team_name):
    team_name.replace(" ", "%20")
    url_search = "https://int.soccerway.com/search/teams/?q=" + team_name
    html_search = requests.get(url_search, headers=HEADERS).text
    soup_search = BeautifulSoup(html_search)
    # soup_search.find("ul", attrs={"class": u"tree search-results"})
    # print(soup_search)

    tbl = soup_search.find_all('ul')
    for e in tbl:
        if e.has_attr('class') and e['class'][0] == 'tree search-results':
            print(e)
            break



def get_team_data(team_id):
    pass
