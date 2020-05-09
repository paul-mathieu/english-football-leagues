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
#
# client = footballAPI.FootballAPI()
# client.tests(parameters_dictionary)
# client.set_parameters(parameters_dictionary)
# client.tests_api_teams()

# print("===============")
# print(client.json_data)
# print("===============")


# ===============================================================
#   Leagues
# ===============================================================
parameters_dictionary = {"API type": "leagues", "country": "england"}  # shows all the competitions in england

# example of additionnal parameters :
# "competitions type": True ( if we want to show the competition type) FAIT
# "winners":True (shows all the team winners through years) FAIT
# "tables" : True (shows the rankings) PAUL va le faire

# pour avoir l'équipe gagnante d'une competition selon les annees
#parameters_dictionary = {"API type": "leagues", "country": "england", "league": "league-one", "winner":True, "end year":"all"}

# pour avoir l'équipe gagnante pour une année
# parameters_dictionary = {"API type": "leagues", "country": "england", "league": "u21-premier-league-division-2", "winner":True, "end year":"all"}

# test gagnant avec la france
# parameters_dictionary = {"API type": "leagues", "country": "france", "league": "ligue-2", "winner":True, "end year":"all"}

# test gagnant en autriche
# parameters_dictionary = {"API type": "leagues", "country": "austria", "league": "bundesliga", "winner":True, "end year":"all"}

# dans certains pays ca marche pas pour la recherche selon une saison particulière car c'est' pas le même format de season Annee/Annee ( des fois juste Annee et des fois les deux)
# par exemple au burkina faso
# y aussi le cas bizarre de el salvador
# faire fonction get id de la competition

# parameters_dictionary = {"API type": "leagues", "country": "england", "type": True}
#parameters_dictionary = {"API type": "leagues", "country": "england", "all": True}
#parameters_dictionary = {"API type": "leagues", "country": "england"}

# tous les parametres
# API type (parameter required)
# country (parameter required)
# league
# all
# type
# winner
# endyear

# User's request :
# to get the winner of league : API type, country, league, winner, end year
# (end year="all" if want winners through all the seasons or the end year (int) to get the winner of this season
# (ex: 2019)
# to get all the competitions of a country with their types : API type, country, league, type OK
# to get all leagues with sub divisions : API type, country, all OK
# to get all the competition of a country: API type, country OK


# il faudrait aussi avoir la liste des équipes par division

client = footballAPI.FootballAPI()
client.set_parameters(parameters_dictionary)
client.tests_api_teams()

print("===============")
print(client.json_data)
print("===============")
