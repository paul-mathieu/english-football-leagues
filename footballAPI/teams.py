# -*- coding: UTF-8 -*-

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
        self.URL = "https://uk.soccerway.com/national/england/premier-league/20192020/regular-season/r53145/tables/"

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
        return BeautifulSoup(urlopen(self.URL), "html.parser").findAll("html")

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








