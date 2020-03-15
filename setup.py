# -*- coding: UTF-8 -*-

import footballAPI


# ===============================================================
#   Players
# ===============================================================


# ===============================================================
#   Teams
# ===============================================================

parameters_dictionary = {"API type": "teams", "country": "england", "league": "league-one", "end year": None}

client = footballAPI.FootballAPI()
client.set_parameters(parameters_dictionary)
print(client.json_data)

# ===============================================================
#   Leagues
# ===============================================================


