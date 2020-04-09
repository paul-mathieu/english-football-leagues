# -*- coding: UTF-8 -*-
import psycopg2

import footballAPI

# ===============================================================
#   Players
# ===============================================================

# parameters_dictionary = {"API type": "players", "lastName": "Majka", "firstName": "Matej"}
# dataBase = ""
# dataBase = psycopg2.connect(host="localhost",database="Foot", user="postgres", password="")

# client = footballAPI.FootballAPI()
# client.set_parameters(parameters_dictionary, dataBase)

# print("===============")
# matches = client.json_data
# print(matches)
# print("===============")


# ===============================================================
#   Teams
# ===============================================================

# parameters_dictionary = {"API type": "teams", "country": "england", "league": "league-one", "end year": 2019}

# client = footballAPI.FootballAPI()
# client.set_parameters(parameters_dictionary)
# client.tests_api_teams()

# print("===============")
# print(client.json_data)
# print("===============")


# ===============================================================
#   Leagues
# ===============================================================

# noah_parameters_dictionary = {"API type": "leagues", "country": "england", "league": "league-one", "end year": 2019}

# test_parameters_dictionnary = {"API type": "leagues", "country": "england" } shows all the competitions in england
# example of additionnal parameters :
# "competitions type": True ( if we want to show the competition type)
# "winners":True (shows all the team winners through years)
# "tables" : True (shows the rankings)

# il faudrait aussi avoir la liste des équipes par division

# client = footballAPI.FootballAPI()
# client.set_parameters(noah_parameters_dictionary)
# client.tests_api_teams()

# print("===============")
# print(client.json_data)
# print("===============")
