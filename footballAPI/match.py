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
        self.request_headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, '
                          'like Gecko) Chrome/53.0.2785.143 Safari/537.36'}




    def set_parameters_dictionary(self, parameters_dictionary):
        """
        Set the query option dictionary
            :param parameters_dictionary: dictionary of values
            :type parameters_dictionary: dict
        """
        self.parameters_dictionary = {"API type": None, "clubA": None, "countryA":None, "clubB": None, "countryB": None, "all":None}
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
        if self.parameters_dictionary["all"] is not None:
            return self.matchWeek()
        elif self.parameters_dictionary["clubA"] is not None and self.parameters_dictionary["clubB"] is not None and self.parameters_dictionary["countryB"] is not None and self.parameters_dictionary["countryA"] is not None:
            return self.proc()
        else:
            return -1



    def proc(self, team1 = '', team2 = '', n1 = '', n2 = ''):
        if team1 == '' and team2 == '' and n1 == '' and n2 == '':
            a = Players()
            a.set_parameters_dictionary({"API type": "players", "country": self.parameters_dictionary["countryA"], "club": self.parameters_dictionary["clubA"]})
            clubA = a.parameters_dictionary["club"]
            teamA = a.json_players(a.parameters_dictionary)
            # print(teamA)


            b = Players()
            b.set_parameters_dictionary({"API type": "players", "country": self.parameters_dictionary["countryB"], "club": self.parameters_dictionary["clubB"]})
            clubB = b.parameters_dictionary["club"]
            teamB = b.json_players(b.parameters_dictionary)

        else:
            teamA = Players().functionProcessing1b(team1)
            clubA = n1

            teamB = Players().functionProcessing1b(team2)
            clubB = n2

            # print("L'équipe a est : ", teamA)

        totalGM_teamA = 0
        totalAge_teamA = 0
        totalGoalA = 0
        totalAssistsA = 0
        totalYellowA = 0
        totalRedA = 0
        i = 0
        v = 0
        for aaa in teamA[0]["TeamPlayer"]:
            totalGM_teamA += int(aaa["game_minutes"])
            if aaa["age"] == '':
                aaa["age"] = 0
                v = 1
            else:
                totalAge_teamA+= int(aaa["age"])
            totalGoalA += int(aaa["number_statistic_goals"])
            totalAssistsA += int(aaa["number_statistic_assists"])
            totalRedA += int(aaa["red_cards"])
            totalYellowA += int(aaa["yellow_cards"])
            i+=1
            # print(i)
        if v == 1:
            ma = 'na'
        else:
            ma = round(totalAge_teamA / i, 2)
        dataTeamA = {
            'club': clubA,
            'gameMinutes': totalGM_teamA,
            'meanGameMinutes': round(totalGM_teamA / i, 2),
            'MeanAge': ma,
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
        v = 0

        for a in teamB[0]["TeamPlayer"]:
            totalGM_teamB += int(a["game_minutes"])

            if a["age"] == '':
                a["age"] = 0
                v = 1
            else:
                totalAge_teamB += int(a["age"])
            totalGoalB += int(a["number_statistic_goals"])
            totalAssistsB += int(a["number_statistic_assists"])
            totalRedB += int(a["red_cards"])
            totalYellowB += int(a["yellow_cards"])
            j += 1


        if v == 1:
            ma = 'na'
        else:
            ma = round(totalAge_teamB / i, 2)
        dataTeamB = {
            'club': clubB,
            'gameMinutes': totalGM_teamB,
            'meanGameMinutes': round(totalGM_teamB / j, 2),
            'MeanAge': ma,
            'Goal': totalGoalB,
            'Assists': totalAssistsB,
            'Red': totalRedB,
            'Yellow': totalYellowB,
            'Date': str(time.localtime().tm_mon) + '/' + str(time.localtime().tm_mday) + '/' + str(time.localtime().tm_year)

        }
        return {"match": [dataTeamA, dataTeamB]}




    def matchWeek(self):
        '''
        This function searches for the matches of the day
        :return: list[dict]
        '''
        aRetourner = []
        a= str(time.localtime().tm_year)

        m= str(time.localtime().tm_mon)
        if len(m) == 1:
            m = "0"+m

        j= str(time.localtime().tm_mday)
        if len(j) == 1:
            j = "0"+j

        URL = BASE_URL+"/matches/"+a+"/"+m+"/"+j
        html = requests.get(URL, headers=self.request_headers)
        html_soup = BeautifulSoup(html.text, 'html.parser')
        rows = html_soup.find_all('table', {"class":"matches date_matches grouped"})
        for row in rows:
            a = row.find_all("tr")
            for b in a:
               id = b.get('id')
               try:
                   for i in range(len(id)):
                       if id[-i] == "-":
                           id = id[-i+1:]
                           getM = "https://uk.soccerway.com/a/block_date_matches?block_id=page_matches_1_block_date_matches_1&callback_params={%22block_service_id%22%3A%22matches_index_block_datematches%22%2C%22date%22%3A%222020-04-28%22%2C%22stage-value%22%3A%" \
                                  "221%22}&action=showMatches&params={%22competition_id%22%3A"+id+"}"
                           req = requests.get(getM, headers = self.request_headers).json()["commands"][0]["parameters"]["content"]
                           html_soup1 = BeautifulSoup(req, 'html.parser')
                           rows = html_soup1.findAll("tr")
                           for row in rows:
                               cells = row.find_all('td')
                               try:
                                   teamAurl = BASE_URL+cells[1].a.get('href')+'squad/'
                                   teamBurl = BASE_URL+cells[3].a.get('href')+'squad/'
                                   aRetourner.append(self.proc(teamAurl,teamBurl, cells[1].text, cells[3].text))
                               except:
                                   pass
               except:
                   pass
        return aRetourner

