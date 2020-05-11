# -*- coding: UTF-8 -*-
from .core import *
from bs4 import BeautifulSoup


def get_team_id(team_name):
    """
    Get the id of a team with the query name
        :param team_name: name of the team (no restrictions)
        :type team_name: str
        :return result: id number of the team
        :rtype result: str
    """
    team_name.replace(" ", "%20")
    url_search = "https://int.soccerway.com/search/teams/?q=" + team_name
    html_search = requests.get(url_search, headers=HEADERS).text
    soup_search = BeautifulSoup(html_search, features="lxml")

    tbl = soup_search.find_all("ul", {"class": "tree"})
    if len(tbl) == 0:
        return None

    result = tbl[0].find_all("li")[0].find_all("a")[0]["href"]
    for part in range(3):
        result = result[result.index("/", 1):]
    result = result[1:len(result) - 1]
    # print(result)

    return result


def get_team_data(team_id):
    output_dictionnary = dict()

    # === INFO ===
    info_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/"
    info_data = get_team_data_info(team_id, info_url)
    output_dictionnary["info"] = info_data

    # === VENUE ===
    venue_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/venue/"
    venue_data = get_team_data_venue(team_id, venue_url)
    output_dictionnary["venue"] = venue_data

    # === TROPHIES ===
    trophies_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/trophies/"
    trophies_data = get_team_data_trophies(team_id, trophies_url)
    output_dictionnary["trophies"] = trophies_data

    # === MATCHES ===
    matches_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/matches/"
    matches_data = get_team_data_matches(team_id, matches_url)
    output_dictionnary["matches"] = matches_data

    # === SQUAD ===
    squad_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/squad/"
    squad_data = get_team_data_squad(team_id, squad_url)
    output_dictionnary["squad"] = squad_data

    # === FAN SITES ===
    fan_sites_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/"
    fan_sites_data = get_team_data_fan_sites(team_id, fan_sites_url)
    output_dictionnary["fan_sites"] = fan_sites_data

    return output_dictionnary


def get_team_data_info(team_id, info_url):
    # variables
    output_dictionnary = dict()
    bf_html_content = get_beautiful_soup(info_url)

    return output_dictionnary if len(output_dictionnary.keys()) > 0 else None


def get_team_data_venue(team_id, venue_url):
    # variables
    output_dictionnary = dict()
    bf_html_content = get_beautiful_soup(venue_url)

    return output_dictionnary if len(output_dictionnary.keys()) > 0 else None


def get_team_data_trophies(team_id, trophies_url):
    # variables
    output_dictionnary = dict()
    bf_html_content = get_beautiful_soup(trophies_url)

    return output_dictionnary if len(output_dictionnary.keys()) > 0 else None


def get_team_data_matches(team_id, matches_url):
    # variables
    output_dictionnary = dict()
    bf_html_content = get_beautiful_soup(matches_url)

    return output_dictionnary if len(output_dictionnary.keys()) > 0 else None


def get_team_data_squad(team_id, squad_url):
    # variables
    output_dictionnary = dict()
    bf_html_content = get_beautiful_soup(squad_url)

    return output_dictionnary if len(output_dictionnary.keys()) > 0 else None


def get_team_data_fan_sites(team_id, fan_sites_url):
    # variables
    output_dictionnary = dict()
    bf_html_content = get_beautiful_soup(fan_sites_url)

    return output_dictionnary if len(output_dictionnary.keys()) > 0 else None


def get_beautiful_soup(base_url):
    html_search = requests.get(base_url, headers=HEADERS).text
    soup_search = BeautifulSoup(html_search, features="lxml")
    return soup_search
