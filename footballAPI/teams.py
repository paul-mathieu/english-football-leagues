# -*- coding: UTF-8 -*-
from .core import *
from .teams_external_getters import *
from bs4 import BeautifulSoup
from urllib.request import urlopen


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
        self.fill_parameters_dictionary(self.parameters_dictionary)
        self.set_url_teams()
        # return BeautifulSoup(urlopen(self.URL), "html.parser").findAll("form")[2]
        print("team name: " + get_team_id("liverpool FC"))
        print("team data: " + get_team_data('663', self.URL))

    # ===============================================================
    #   Prints and debugs
    # ===============================================================

    def display_teams(self):
        # print("URL: ", self.URL, sep="")

        rows = self.get_table_teams()
        # print(rows[0])

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
        # print(url)

    def tests(self, parameters_dictionary):
        self.set_parameters_dictionary(parameters_dictionary)
        self.display_teams()





