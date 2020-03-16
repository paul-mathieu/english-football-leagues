# -*- coding: UTF-8 -*-

from .core import *


class Players(object):
    ""

    def __init__(self, *args):
        self.parameters_dictionary = None
        self.URL = None

    def set_parameters_dictionary(self, parameters_dictionary):
        print(parameters_dictionary)
        self.parameters_dictionary = parameters_dictionary

    def set_URL_Players(self):
        """
        Exemple of URL : https://fr.soccerway.com/teams/england/liverpool-fc/ - In this configuration, the function returns the teams of the chosen club
        :return:
        """

        self.URL = BASE_URL + "/teams/" + self.parameters_dictionary["country"] + "/" + self.parameters_dictionary[
            "club"] + "/"
        print(self.URL)

    def display(self):
        print(get_HTML(self.URL))
        print("\n\n\n" + self.URL)

    def json_players(self, parameters_dictionary):
        self.set_parameters_dictionary(parameters_dictionary)
        self.set_URL_Players()
        self.processing()
        # self.display()

    def processing(self):
        if ((self.parameters_dictionary["country"] != None) and (self.parameters_dictionary["club"] != None)):
            HTML_p = get_HTML(self.URL).splitlines()
            teamStart = False
            teamTab = False
            for i in HTML_p:
                if ("table squad sortable" in i):
                    teamStart = True
                if ("Fansites" in i):
                    teamStart = False
                if ("<table " in i):
                    teamTab = True
                if ("</table>" in i):
                    teamTab = False
                if (teamStart == True and teamTab == True):
                    print(i)


