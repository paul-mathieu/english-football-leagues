# -*- coding: UTF-8 -*-

from .core import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


class Players(object):
    """

    """

    def __init__(self, *args):
        self.parameters_dictionary = None
        self.URL = None

    def set_parameters_dictionary(self, parameters_dictionary):
        print(parameters_dictionary)
        self.parameters_dictionary = parameters_dictionary

    def set_URL_Players(self):
        """
        :return:
        """
        self.URL = BASE_URL + "/teams/" + self.parameters_dictionary["country"] + "/" + self.parameters_dictionary["club"] + "/squad/"
        print(self.URL)


    def display(self):
        print(get_HTML(self.URL))
        print("\n\n\n" + self.URL)



    def json_players(self, parameters_dictionary):
        self.set_parameters_dictionary(parameters_dictionary)
        self.set_URL_Players()
        return self.processing()
        # self.display()



    def processing(self):
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