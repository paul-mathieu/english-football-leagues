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
    """
    get data for a team
        :param team_id: id of a team on the site soccerway.com
        :type team_id: str
        :return output_dictionary: dictionnary with all infos of a team
        :rtype output_dictionary: dict
    """
    output_dictionary = dict()

    # === INFO ===
    info_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/"
    info_data = get_team_data_info(team_id, info_url)
    output_dictionary["info"] = info_data

    # === VENUE ===
    venue_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/venue/"
    venue_data = get_team_data_venue(team_id, venue_url)
    output_dictionary["venue"] = venue_data

    # === TROPHIES ===
    trophies_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/trophies/"
    trophies_data = get_team_data_trophies(team_id, trophies_url)
    output_dictionary["trophies"] = trophies_data

    # === MATCHES ===
    matches_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/matches/"
    matches_data = get_team_data_matches(team_id, matches_url)
    output_dictionary["matches"] = matches_data

    # === SQUAD ===
    squad_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/squad/"
    squad_data = get_team_data_squad(team_id, squad_url)
    output_dictionary["squad"] = squad_data

    # === TRANSFERS ===
    transfers_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/transfers/"
    transfers_data = get_team_data_transfers(team_id, transfers_url)
    output_dictionary["squad"] = transfers_data

    # === FAN SITES ===
    fan_sites_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/"
    fan_sites_data = get_team_data_fan_sites(team_id, fan_sites_url)
    output_dictionary["fan_sites"] = fan_sites_data

    return output_dictionary


def get_team_data_info(team_id, info_url):
    """
    Getter which allows to obtain a dictionary with the information of a team:
 
        :param team_id: id of the team
        :type team_id: str
        :param info_url: url for get info
        :type info_url: str
        :return output_dictionary: dictionary data with all info of the team
        :rtype output_dictionary: dict or None
    """
    # variables
    output_dictionary = dict()
    bf_html_content = get_beautiful_soup(info_url)

    return output_dictionary if len(output_dictionary.keys()) > 0 else None


def get_team_data_venue(team_id, venue_url):
    """
    Getter which allows to obtain a dictionary with the information of a team:
 
        :param team_id: id of the team
        :type team_id: str
        :param venue_url: url for get venue
        :type venue_url: str
        :return output_dictionary: dictionary data with all venue of the team
        :rtype output_dictionary: dict or None
    """
    # variables
    output_dictionary = dict()
    bf_html_content = get_beautiful_soup(venue_url)

    return output_dictionary if len(output_dictionary.keys()) > 0 else None


def get_team_data_trophies(team_id, trophies_url):
    """
    Getter which allows to obtain a dictionary with the information of a team:
 
        :param team_id: id of the team
        :type team_id: str
        :param trophies_url: url for get trophies
        :type trophies_url: str
        :return output_dictionary: dictionary data with all trophies of the team
        :rtype output_dictionary: dict or None
    """
    # variables
    output_dictionary = dict()
    bf_html_content = get_beautiful_soup(trophies_url)

    return output_dictionary if len(output_dictionary.keys()) > 0 else None


def get_team_data_matches(team_id, matches_url):
    """
    Getter which allows to obtain a dictionary with the information of a team:
 
        :param team_id: id of the team
        :type team_id: str
        :param matches_url: url for get matches
        :type matches_url: str
        :return output_dictionary: dictionary data with all matches of the team
        :rtype output_dictionary: dict or None
    """
    # variables
    output_dictionary = dict()
    bf_html_content = get_beautiful_soup(matches_url)

    return output_dictionary if len(output_dictionary.keys()) > 0 else None


def get_team_data_squad(team_id, squad_url):
    """
    Getter which allows to obtain a dictionary with the information of a team:
 
        :param team_id: id of the team
        :type team_id: str
        :param squad_url: url for get squad
        :type squad_url: str
        :return output_dictionary: dictionary data with all squad of the team
        :rtype output_dictionary: dict or None
    """
    # variables
    output_dictionary = dict()
    bf_html_content = get_beautiful_soup(squad_url)

    return output_dictionary if len(output_dictionary.keys()) > 0 else None


def get_team_data_transfers(team_id, transfers_url):
    """
    Getter which allows to obtain a dictionary with the information of a team:
 
        :param team_id: id of the team
        :type team_id: str
        :param transfers_url: url for get transfers
        :type transfers_url: str
        :return output_dictionary: dictionary data with all transfers of the team
        :rtype output_dictionary: dict or None
    """
    # variables
    output_dictionary = dict()
    bf_html_content = get_beautiful_soup(transfers_url)

    return output_dictionary if len(output_dictionary.keys()) > 0 else None


def get_team_data_fan_sites(team_id, fan_sites_url):
    """
    Getter which allows to obtain a dictionary with the information of a team:
 
        :param team_id: id of the team
        :type team_id: str
        :param fan_sites_url: url for get fan sites
        :type fan_sites_url: str
        :return output_dictionary: dictionary data with all fan sites of the team
        :rtype output_dictionary: dict or None
    """
    # variables
    output_dictionary = dict()
    bf_html_content = get_beautiful_soup(fan_sites_url)

    return output_dictionary if len(output_dictionary.keys()) > 0 else None


def get_beautiful_soup(base_url):
    html_search = requests.get(base_url, headers=HEADERS).text
    soup_search = BeautifulSoup(html_search, features="lxml")
    return soup_search
