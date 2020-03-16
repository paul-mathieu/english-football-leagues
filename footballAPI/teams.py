# -*- coding: UTF-8 -*-

from .core import *
from bs4 import BeautifulSoup


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
        self.parameters_dictionary = parameters_dictionary
        # print("test")

    def set_URL_teams(self):
        """
        Set the URL for the request
        """
        self.URL = BASE_URL + TEAMS_START_URL + \
                   "/" + self.parameters_dictionary["country"] + \
                   "/" + self.parameters_dictionary["league"] + \
                   "/" + get_year(self.parameters_dictionary) + \
                   TEAMS_END_URL

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
        self.display()

    # ===============================================================
    #   Prints and debugs
    # ===============================================================

    def display(self):
        print(get_HTML(self.URL))
