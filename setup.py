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

#pour avoir l'équipe gagnante d'une competition selon les annees
#parameters_dictionnary = {"API type": "leagues", "country": "england", "league": "league-one", "winner":True, "end year":"all"}

#pour avoir l'équipe gagnante pour une année
#parameters_dictionnary = {"API type": "leagues", "country": "england", "league": "premier-league", "winner":True, "end year":1889}

#faire fonction get id de la competition

# il faudrait aussi avoir la liste des équipes par division

# client = footballAPI.FootballAPI()
# client.set_parameters(parameters_dictionnary)
# client.tests_api_teams()

# print("===============")
# print(client.json_data)
# print("===============")
