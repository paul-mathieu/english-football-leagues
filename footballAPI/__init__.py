# -*- coding: UTF-8 -*-

"""
    football
    ----------
    Football API for Python

    :copyright: (c) 2020 by VieuL paul-mathieu NoahRz
"""
import psycopg2

from .core import *
from .players import Players
from .teams import Teams
from .leagues import Leagues
from .dataBase import dataBase

class FootballAPI(Players, Teams, Leagues):
    """
    The queries in this FootballAPI class are used to obtain or 
    extract a json file according to user-defined parameters.
    """

    # ===============================================================
    #   Initialisation
    # ===============================================================

    def __init__(self, *args):
        """
        Initialization of the FootballAPI class with call of the children classes
            :param args: others arg (not necessary)
        """
        Players.__init__(self, *args)
        Teams.__init__(self, *args)
        Leagues.__init__(self, *args)
        self.json_data = None
        self.db = None
    # ===============================================================
    #   Setters
    # ===============================================================

    def set_parameters(self, parameters_dictionary, db = None):
        """
        Add the dictionary attribute for the values of the query and
        apply the method which adds the json attribute of the values
        obtained after the query.
            :param parameters_dictionary: dictionary of values
            :type parameters_dictionary: dict
        """
        self.parameters_dictionary = parameters_dictionary
        self.db = db
        self.set_json_data()


    def set_json_data(self):
        """
        Applies the query based on dictionary settings.
        The request can apply to players, teams or leagues.
        """
        print(type(self.db))



        if is_players_request(self.parameters_dictionary):
            self.json_data = self.json_players(self.parameters_dictionary)
        elif is_teams_request(self.parameters_dictionary):
            self.json_data = self.json_teams(self.parameters_dictionary)
        elif is_leagues_request(self.parameters_dictionary):
            self.json_data = self.json_leagues(self.parameters_dictionary)

        if type(self.db) is psycopg2.extensions.connection:
            a = dataBase(self.db,self.json_data)
            a.processing()
# ===============================================================
#   Links
# ===============================================================

__copyright__ = "Copyright 2020 by VieuL paul-mathieu NoahRz"
__authors__ = ["paul-mathieu", "NoahRz", "VieuL"]
__source__ = "https://github.com/paul-mathieu/English-football-leagues-API"
__license__ = "MIT"

__all__ = ["Players", "Teams", "Leagues"]
