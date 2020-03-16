# -*- coding: UTF-8 -*-

import footballAPI


# ===============================================================
#   Players
# ===============================================================

# parameters_dictionary = {"API type": "players", "country": "england", "club": "liverpool-fc"}
#
# client = footballAPI.FootballAPI()
# client.set_parameters(parameters_dictionary)
#
# print("===============")
# print(client.json_data)
# print("===============")


# ===============================================================
#   Teams
# ===============================================================

parameters_dictionary = {"API type": "teams", "country": "england", "league": "league-one", "end year": 2019}

client = footballAPI.FootballAPI()
client.set_parameters(parameters_dictionary)

print("===============")
print(client.json_data)
print("===============")


# ===============================================================
#   Leagues
# ===============================================================


