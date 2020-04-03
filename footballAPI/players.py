# -*- coding: UTF-8 -*-

from .core import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests


class Players(object):
    """

    """
    # ===============================================================
    #   Initialisation
    # ===============================================================
    def __init__(self, *args):
        self.parameters_dictionary = None
        self.URL = None
        self.choix = 0

    def set_parameters_dictionary(self, parameters_dictionary):
        self.parameters_dictionary = {"API type": None, "country": None, "league": None, "end year": None, "club": None, "firstName": None, "lastName": None }
        self.fill_parameters_dictionary(parameters_dictionary)



    # ===============================================================
    #   Setters
    # ===============================================================
    def set_URL_Players(self):
        """
        :return:
        """
        print(self.parameters_dictionary)
        if self.parameters_dictionary["country"] != None and self.parameters_dictionary["club"] != None:
            self.URL = BASE_URL + "/teams/" + self.parameters_dictionary["country"] + "/" + self.parameters_dictionary["club"] + "/squad/"
            self.choix = 1
        if self.parameters_dictionary["firstName"] != None and self.parameters_dictionary["lastName"] != None:
            param = str(self.parameters_dictionary["lastName"]).replace(" ","+")
            self.URL = BASE_URL + "/search/?q=" + param
            self.choix = 2
        print(self.URL)


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

    def display(self):
        print(get_HTML(self.URL))
        print("\n\n\n" + self.URL)



    def json_players(self, parameters_dictionary):
        self.set_parameters_dictionary(parameters_dictionary)
        self.set_URL_Players()
        return self.processing()
        # self.display()


    # ===============================================================
    # ============================ Core =============================
    # ===============================================================
    def processing(self):

        # If we search a team squad
        if self.choix == 1:
            html = urlopen(self.URL)
            html_soup = BeautifulSoup(html, 'html.parser')
            rows = html_soup.findAll("tr")
            players = []
            for row in rows:
                cells = row.findAll("td")
                # print(cells)
                # print("\n\n")
                if len(cells) == 17:
                    try:
                        players_entry = {
                            "shirtnumber": cells[0].text,
                            "name": cells[2].text,
                            "age": cells[4].text,
                            "position": cells[5].text,
                            "game-minutes" : cells[6].text,
                            "appearances" : cells[7].text,
                            "lineups": cells[8].text,
                            "subs-in": cells[9].text,
                            "subs-out": cells[10].text,
                            "subs-on-bench": cells[11].text,
                            "number statistic goals" : cells[12].text,
                            "number statistic assists" : cells[13].text,
                            "yellow - cards" : cells[14].text,
                            "2nd-yellow-cards": cells[15].text,
                            "red-cards": cells[16].text
                        }
                        players.append(players_entry)
                    except:
                        pass
            return players

        # If we search a player
        if self.choix == 2:
            html = urlopen(self.URL)
            html_soup = BeautifulSoup(html, 'html.parser')
            rows = html_soup.findAll("tr")
            del html, html_soup
            find = False
            for row in rows:
                cells = row.findAll("td")
                try:
                    if str(self.parameters_dictionary["firstName"]).upper() in str(cells[0].text).upper():
                        print("Player name is ",cells[0].text)
                        playerUrl = BASE_URL + "/" + str(cells[0].a.get('href'))
                        find = True
                        break;
                except:
                    pass
            if(find != True): raise ValueError("Player name not found")
            html = urlopen(playerUrl)
            html_soup = BeautifulSoup(html, 'html.parser')
            # print(html_soup)
            print(playerUrl)
            numPlayerL = playerUrl.split("/")[-2]
            matchs = []
            # A mettre dans une boucle pour charger l'ensemble des pages
            exe = 1
            i = 0
            while exe != 0:
                getMeth = 'https://uk.soccerway.com/a/block_player_matches?block_id=page_player_1_block_player_matches_3&callback_params=%7B%22page%22%3A0%2C%22block_service_id%22%3A%22player_matches_block_playermatches%22%2C%22people_id%22%3A'+numPlayerL+'%2C%22type%22%3Anull%2C%22formats%22%3Anull%7D&action=changePage&params=%7B%22page%22%3A'+str(i)+'%7D'
                listGetMeth = getMeth.split("%")
                # print(listGetMeth)

                htmlMatchs = requests.get(getMeth).json()["commands"][0]["parameters"]["content"]
                print(htmlMatchs)
                if len(str(htmlMatchs)) < 100:
                    return matchs

                html_soup = BeautifulSoup(htmlMatchs, 'html.parser')
                rows = html_soup.findAll("tr")

                for row in rows:
                    cells = row.findAll("td")
                    try:
                        Match = {
                            "Date": cells[1].text,
                            "Ligue": cells[2].text,
                            "winerTeam": cells[3].text,
                            "Score": cells[4].text,
                            "loserTeam": cells[5].text,
                            }
                        matchs.append(Match)
                        print(Match)

                    except:
                        pass
                i = i-1
            pass