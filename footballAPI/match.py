import time

from .core import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime
from .players import *
class Match(object):
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
        self.parameters_dictionary = {"API type": None, "clubA": None, "countryA":None, "clubB": None, "countryB": None}
        self.fill_parameters_dictionary(parameters_dictionary)

    def fill_parameters_dictionary(self, parameters_dictionary):
        """
        Fill the attribute parameters_dictionary
            :param parameters_dictionary: dictionary of query parameters
            :type parameters_dictionary: dict
        """
        for key in parameters_dictionary.keys():
                self.parameters_dictionary[key] = parameters_dictionary[key]






    def json_match(self, parameters_dictionary):
        """
        Apply the query with parameters and return a dictionary (json)
            :param parameters_dictionary: dictionary of query parameters
            :type parameters_dictionary: dict
            :return json_data: json data
            :rtype json_data: dict
        """
        self.set_parameters_dictionary(parameters_dictionary)
        return self.proc()

    def proc(self):
        a = Players()
        a.set_parameters_dictionary({"API type": "players", "country": self.parameters_dictionary["countryA"], "club": self.parameters_dictionary["clubA"]})
        clubA = a.parameters_dictionary["club"]
        teamA = a.json_players(a.parameters_dictionary)
        # print(teamA)

        print("\n\n ------------------------- \n\n")

        b = Players()
        b.set_parameters_dictionary({"API type": "players", "country": self.parameters_dictionary["countryB"], "club": self.parameters_dictionary["clubB"]})
        clubB = b.parameters_dictionary["club"]
        teamB = b.json_players(b.parameters_dictionary)
        # print(teamB)
        totalGM_teamA = 0
        totalAge_teamA = 0
        totalGoalA = 0
        totalAssistsA = 0
        totalYellowA = 0
        totalRedA = 0
        i = 0
        for a in teamA[0]["TeamPlayer"]:
            totalGM_teamA += int(a["game_minutes"])
            totalAge_teamA+= int(a["age"])
            totalGoalA += int(a["number_statistic_goals"])
            totalAssistsA += int(a["number_statistic_assists"])
            totalRedA += int(a["red_cards"])
            totalYellowA += int(a["yellow_cards"])
            i+=1
        dataTeamA = {
            'club': clubA,
            'gameMinutes': totalGM_teamA,
            'meanGameMinutes': round(totalGM_teamA / i, 2),
            'MeanAge': round(totalAge_teamA / i, 2),
            'Goal': totalGoalA,
            'Assists': totalAssistsA,
            'Red': totalRedA,
            'Yellow': totalYellowA,
            'Date':  str(time.localtime().tm_mon) +'/'+ str(time.localtime().tm_mday) + '/' +  str(time.localtime().tm_year)
        }


        totalGM_teamB = 0
        totalAge_teamB = 0
        totalGoalB = 0
        totalAssistsB = 0
        totalYellowB = 0
        totalRedB = 0
        j = 0
        for a in teamB[0]["TeamPlayer"]:
            totalGM_teamB += int(a["game_minutes"])
            totalAge_teamB += int(a["age"])
            totalGoalB += int(a["number_statistic_goals"])
            totalAssistsB += int(a["number_statistic_assists"])
            totalRedB += int(a["red_cards"])
            totalYellowB += int(a["yellow_cards"])
            j += 1

        dataTeamB = {
            'club': clubB,
            'gameMinutes': totalGM_teamB,
            'meanGameMinutes': round(totalGM_teamB / j, 2),
            'MeanAge': round(totalAge_teamB / j, 2),
            'Goal': totalGoalB,
            'Assists': totalAssistsB,
            'Red': totalRedB,
            'Yellow': totalYellowB,
            'Date': str(time.localtime().tm_mon) + '/' + str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_year)

        }
        # print(dataTeamA, "\n", dataTeamB)
        return {"match": [dataTeamA, dataTeamB]}
