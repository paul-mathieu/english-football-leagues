# -*- coding: UTF-8 -*-

from .core import *
from bs4 import BeautifulSoup


class Leagues(object):

    def __init__(self, *args):
        pass

    def json_leagues(self, parameters_dictionary):
        self.set_parameters_dictionary_leagues(parameters_dictionary)
        self.set_URL_leagues()
        # self.display_leagues()
        self.getleagues()

    def set_parameters_dictionary_leagues(self, parameters_dictionary):
        self.parameters_dictionary = parameters_dictionary
        # print("test")

    def set_URL_leagues(self):
        self.URL = BASE_URL + LEAGUES_START_URL + \
                   "/" + self.parameters_dictionary["country"] + \
                   "/" + self.parameters_dictionary["league"] + \
                   "/" + self.get_year() + \
                   LEAGUES_END_URL

    def get_year(self):
        if "start year" in self.parameters_dictionary.keys():
            year = int(self.parameters_dictionary["start year"])
            return str(year) + str(year + 1)
        elif "end year" in self.parameters_dictionary.keys():
            year = int(self.parameters_dictionary["end year"])
            return str(year - 1) + str(year)
        else:
            return str(THIS_YEAR - 1) + str(THIS_YEAR)

    def display_leagues(self):
        print("url :", self.URL)
        print(get_HTML(self.URL))

    def getleagues(self):
        html = get_HTML(self.URL)
        html_soup = BeautifulSoup(html, 'html.parser')
        print("leagues1")
        for league in html_soup.find_all('li', class_='even'):
            try:
                title_league = league.a['title']
                print("league_title :", title_league)
            except KeyError:
                pass
        