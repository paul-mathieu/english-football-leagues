# -*- coding: UTF-8 -*-

import footballAPI


# ===============================================================
#   Players
# ===============================================================


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


