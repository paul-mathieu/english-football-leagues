# -*- coding: UTF-8 -*-
import json
import os

import requests
import datetime
import pandas as pd
from pathlib import Path


BASE_URL = "https://uk.soccerway.com"

PLAYERS_URL = None

TEAMS_START_URL = "/national"
TEAMS_END_URL = "/regular-season/tables"

LEAGUES_START_URL = "/national"
LEAGUES_END_URL = "/regular-season"

THIS_YEAR = int(str(datetime.datetime.now())[:4])

HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, '
                         'like Gecko) Chrome/53.0.2785.143 Safari/537.36'}


def get_HTML(url, convert_to_json=False):
    html_content = requests.get(url).text
    if not convert_to_json:
        return html_content
    else:
        return json.loads(json.dumps(html_content))


def is_players_request(parameters_dictionary):
    if "API type" not in parameters_dictionary.keys():
        return False
    return parameters_dictionary["API type"] in ["players", "Players", "PLAYERS"]


def is_teams_request(parameters_dictionary):
    if "API type" not in parameters_dictionary.keys():
        return False
    return parameters_dictionary["API type"] in ["teams", "Teams", "TEAMS"]


def is_leagues_request(parameters_dictionary):
    if "API type" not in parameters_dictionary.keys():
        return False
    return parameters_dictionary["API type"] in ["leagues", "Leagues", "LEAGUES"]

def is_match_request(parameters_dictionary):
    if "API type" not in parameters_dictionary.keys():
        return False
    return parameters_dictionary["API type"] in ["match", "Match", "MATCH"]

def is_transferMarkt_request(parameters_dictionary):
    if "API type" not in parameters_dictionary.keys():
        return False
    return parameters_dictionary["API type"] in ["transfer", "Transfer", "TRANSFER"]


def get_year(parameters_dictionary):
    """
    Returns the year as a season
        :return: two years pasted (ex: 20192020)
        :rtype: str
    """
    if "start year" in parameters_dictionary.keys():
        year = int(parameters_dictionary["start year"])
        return str(year) + str(year + 1)
    elif "end year" in parameters_dictionary.keys():
        year = int(parameters_dictionary["end year"])
        return str(year - 1) + str(year)
    else:
        return str(THIS_YEAR - 1) + str(THIS_YEAR)


def keys_from_first_row(row):
    """
    Returns the list keys of the first row for a table
        :param row: first row of an html table
        :return: name list
        :rtype: list of string
    """
    keys_list = []
    for col_name in row["tr"]["th"]:
        if "@title" in col_name.keys():
            keys_list.append(col_name["@title"])
        elif "#text" in col_name.keys():
            keys_list.append(col_name["#text"])
        elif "acronym" in col_name.keys():
            keys_list.append(col_name["acronym"])
    return keys_list


def data_visualization_general(data):
    """
    transform the data (json object) to csv file and save it in the jupyter_notebook folder
    :param data: json object
    """
    path_to_save = str(Path(__file__).parent.parent) + '/jupyter_notebook/'
    key = list(data.keys())[0]  # we do this way because keys() return a dict-keys which is not subscriptable
    df = pd.DataFrame(data[key])
    file_name = key+".csv"
    df.to_csv(os.path.join(path_to_save, file_name))
    # we save it in the jupyter_notebook folder so that it will be easier to show data on jupyter notebook
