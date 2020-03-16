# -*- coding: UTF-8 -*-

"""
    football
    ----------
    Football API for Python

    :copyright: (c) 2020 by [entrez vos pseudos github] paul-mathieu
"""

from .core import *
from .players import Players
from .teams import Teams
from .leagues import Leagues


class FootballAPI(Players, Teams, Leagues):

    def __init__(self, *args):
        Players.__init__(self, *args)
        Teams.__init__(self, *args)
        Leagues.__init__(self, *args)
        self.json_data = None

    def set_parameters(self, parameters_dictionary):
        self.parameters_dictionary = parameters_dictionary
        self.set_json_data()

    def set_json_data(self):

        print("test 2")
        if is_players_request(self.parameters_dictionary):
            self.json_data = self.json_players(self.parameters_dictionary)

        elif is_teams_request(self.parameters_dictionary):
            self.json_data = self.json_teams(self.parameters_dictionary)

        elif is_leagues_request(self.parameters_dictionary):
            self.json_data = self.json_leagues(self.parameters_dictionary)


__copyright__ = "Copyright 2016 by [entrez vos pseudos github] paul-mathieu"
__authors__ = ["paul-mathieu", "[entrez vos pseudos github]"]
__source__ = "https://github.com/paul-mathieu/English-football-leagues-API"
__license__ = "MIT"

__all__ = ["Football", "API", ]
