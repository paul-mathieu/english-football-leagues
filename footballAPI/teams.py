# -*- coding: UTF-8 -*-

from .core import *
from bs4 import BeautifulSoup


class Teams(object):
    """
    utl type : https://uk.soccerway.com/national/england/league-one/20182019/regular-season/r48115/tables/
      -> https://uk.soccerway.com/national/[country]/[League]/[yearyear]/regular-season/tables
    """

    def __init__(self, *args):
        self.parameters_dictionary = None
        self.URL = None
        # print('init')

    def json_teams(self, parameters_dictionary):
        self.set_parameters_dictionary(parameters_dictionary)
        self.set_URL()
        self.display()

    def set_parameters_dictionary(self, parameters_dictionary):
        self.parameters_dictionary = parameters_dictionary
        # print("test")

    def set_URL(self):
        self.URL = BASE_URL + TEAMS_START_URL + \
                   "/" + self.parameters_dictionary["country"] + \
                   "/" + self.parameters_dictionary["league"] + \
                   "/" + self.get_year() + \
                   TEAMS_END_URL

    def get_year(self):
        if "start year" in self.parameters_dictionary.keys():
            year = int(self.parameters_dictionary["start year"])
            return str(year) + str(year + 1)
        elif "end year" in self.parameters_dictionary.keys():
            year = int(self.parameters_dictionary["end year"])
            return str(year - 1) + str(year)
        else:
            return str(THIS_YEAR - 1) + str(THIS_YEAR)

    def display(self):
        print(get_HTML(self.URL))
