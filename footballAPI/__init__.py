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
from .match import Match
from .transferMarkt import TransferMarkt


class FootballAPI(Players, Teams, Leagues, Match, TransferMarkt):
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
        Match.__init__(self, *args)
        TransferMarkt.__init__(self, *args)
        self.json_data = None
        self.db = None

    # ===============================================================
    #   Setters
    # ===============================================================

    def set_parameters(self, parameters_dictionary, db=None):
        """
        Add the dictionary attribute for the values of the query and
        apply the method which adds the json attribute of the values
        obtained after the query.
            :param db:
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
        if is_players_request(self.parameters_dictionary):
            self.json_data = self.json_players(self.parameters_dictionary)
        elif is_teams_request(self.parameters_dictionary):
            self.json_data = self.json_teams(self.parameters_dictionary)
        elif is_leagues_request(self.parameters_dictionary):
            self.json_data = self.json_leagues(self.parameters_dictionary)
        elif is_match_request(self.parameters_dictionary):
            self.json_data = self.json_match(self.parameters_dictionary)
        elif is_transferMarkt_request(self.parameters_dictionary):
            self.json_data = self.json_transferMarkt(self.parameters_dictionary)

        if type(self.db) is psycopg2.extensions.connection:
            if type(self.json_data) is list:
                for i in range(len(self.json_data)):
                    print(self.json_data[i])
                    print("-------------------------------------")
                    a = dataBase(self.db,self.json_data[i])
                    a.processing()
            if type(self.json_data) is dict:
                for µ in self.json_data:
                    data = self.json_data[µ]
                    data = {µ : data}
                    a = dataBase(self.db, data)
                    a.processing()

    def jsonExit(self, path):
        '''

        :param path: the path to your file
        :return: json file
        '''
        if type(self.json_data) is dict:
            with open(path, 'w') as fp:
                json.dump(self.json_data, fp)
        elif type(self.json_data) is list:
            with open(path, 'w') as fp:
                json.dump(self.json_data, fp)
        else:
            raise ValueError("Json_data type not found")

    def csvExit(self):
        """
        transform the data (json object) to csv file and save it in the jupyter_notebook folder
        :param data: json object
        """
        for µ in self.json_data:
            data = self.json_data[µ]
            data = {µ: data}
            path_to_save = str(Path(__file__).parent.parent) + '/jupyter_notebook/'
            key = list(data.keys())[0]  # we do this way because keys() return a dict-keys which is not subscriptable
            df = pd.DataFrame(data[key])
            file_name = key + ".csv"
            df.to_csv(os.path.join(path_to_save, file_name))

# ===============================================================
#   Links
# ===============================================================

__copyright__ = "Copyright 2020 by VieuL paul-mathieu NoahRz"
__authors__ = ["paul-mathieu", "NoahRz", "VieuL"]
__source__ = "https://github.com/paul-mathieu/English-football-leagues-API"
__license__ = "MIT"

__all__ = ["Players", "Teams", "Leagues"]
