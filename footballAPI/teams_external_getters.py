# -*- coding: UTF-8 -*-
from .core import *
from bs4 import BeautifulSoup
from .players import Players


# ===============================================================
#   Main functions
# ===============================================================

def get_team_id(team_name):
    """
    Get the id of a team with the query name
        :param team_name: name of the team (no restrictions)
        :type team_name: str
        :return result: id number of the team
        :rtype result: str
    """
    output_list = []
    team_name.replace(" ", "%20")
    url_search = "https://int.soccerway.com/search/teams/?q=" + team_name
    html_search = requests.get(url_search, headers=HEADERS).text
    soup_search = BeautifulSoup(html_search, features="lxml")

    tbl = soup_search.find_all("div", {"class": "block_search_results_teams-wrapper"})[0]
    # print(tbl['class'])
    tbl = tbl.find_all("div", {"class": "block_search_results_teams"})[0]
    # print(tbl['class'])
    tbl = tbl.find_all("ul", {"class": "tree"})[0]
    # print(tbl['class'])

    if len(tbl) == 0:
        return None

    lis = tbl.find_all("li")
    for li in lis:
        try:
            result = li.find_all("a")[0]["href"]
            for part in range(3):
                result = result[result.index("/", 1):]
            result = result[1:len(result) - 1]
            output_list.append(result)

        except:
            pass

    return [e for e in output_list if int(e) < 20000]


def get_team_data(team_id,
                  info=False, venue=False,
                  trophies=False, matches=False,
                  squad=False, squad_info=None, fan_sites=False):
    """
    Get wanted data for a team
        :param team_id: id of a team on the site soccerway.com
        :type team_id: str
        :param info: can be specify
        :type info: bool
        :param venue: can be specify
        :type venue: bool
        :param trophies: can be specify
        :type trophies: bool
        :param matches: can be specify
        :type matches: bool
        :param squad: can be specify
        :type squad: bool
        :param squad_info: parameters dict for players
        :type squad_info: dict
        :param fan_sites: can be specify
        :type fan_sites: bool
        :return output_dictionary: dictionnary with all infos of a team
        :rtype output_dictionary: dict
    """
    output_dictionary = dict()

    # v === INFO ===
    if info:
        try:
            info_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/"
            info_data = get_team_data_info(info_url)
            output_dictionary["info"] = info_data
        except:
            output_dictionary["info"] = None

    # v === VENUE ===
    if venue:
        try:
            venue_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/venue/"
            venue_data = get_team_data_venue(venue_url)
            output_dictionary["venue"] = venue_data
        except:
            output_dictionary["info"] = None

    # v === TROPHIES ===
    if trophies:
        try:
            trophies_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/trophies/"
            trophies_data = get_team_data_trophies(trophies_url)
            output_dictionary["trophies"] = trophies_data
        except:
            output_dictionary["info"] = None

    # v === MATCHES ===
    if matches:
        try:
            matches_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/matches/"
            matches_data = get_team_data_matches(matches_url)
            output_dictionary["matches"] = matches_data
        except:
            output_dictionary["info"] = None

    # === SQUAD ===
    if squad:
        try:
            if squad_info is None:
                squad_info = {}
            squad_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/squad/"
            squad_data = get_team_data_squad(team_id, squad_url, squad_info)
            output_dictionary["squad"] = squad_data
        except:
            output_dictionary["info"] = None

    # v === FAN SITES ===
    if fan_sites:
        try:
            fan_sites_url = "https://int.soccerway.com/teams/england/x/" + str(team_id) + "/"
            fan_sites_data = get_team_data_fan_sites(team_id, fan_sites_url)
            output_dictionary["fan_sites"] = fan_sites_data
        except:
            output_dictionary["info"] = None

    return output_dictionary


# ===============================================================
#   Functions to recover different types of data
# ===============================================================

def get_team_data_info(info_url):
    """
    Getter which allows to obtain a dictionary with the information of a team:
        - date of foundation of the club
        - club address
        - club country
        - club telephone
        - club fax
        - E-mail adress
        :param info_url: url for get info
        :type info_url: str
        :return output_dictionary: dictionary data with all info of the team
        :rtype output_dictionary: dict or None
    """
    # variables
    output_dictionary = dict()
    bf_html_content = get_beautiful_soup(info_url)

    tbl = bf_html_content.find_all("div", {"class": "block_team_info"})
    if len(tbl) == 0:
        return None
    tbl = tbl[0]

    # part logo of the club
    tbl_img = tbl.find_all("img")
    if len(tbl_img) > 0:
        output_dictionary["logo"] = tbl_img[0]["src"]

    # part info club
    tbl_info = tbl.find_all("dl")
    if len(tbl_info) > 0:
        dl = tbl_info[0]

        # keys of the dict
        dt_list = dl.find_all("dt")
        dt_content_list = [str(e)[4:-5] for e in dt_list]
        # values of the dict
        dd_list = dl.find_all("dd")
        dd_content_list = [str(e)[4:-5] for e in dd_list]

        # replace unexpected characters
        for content_list in [dd_content_list, dt_content_list]:
            for index in range(len(content_list)):
                content_list[index] = content_list[index].replace("  ", "")
                content_list[index] = content_list[index].replace("\n", "")
                content_list[index] = content_list[index].replace("<br/>", ", ")

        for index in range(len(dd_content_list)):
            output_dictionary[dt_content_list[index]] = dd_content_list[index]

        try:
            a = output_dictionary['E-mail']
            b = "\">"
            c = "</a>"
            output_dictionary['E-mail'] = a[a.index(b) + len(b):a.index(c)]
        except:
            pass

    return output_dictionary if len(output_dictionary.keys()) > 0 else None


def get_team_data_venue(venue_url):
    """
    Getter which allows to obtain a dictionary with the information of a team:
        - address
        - zip code of the stadium
        - stadium city
        - stadium phone
        - stadium capacity
        - type of stadium area
        - map and location of the stadium on google maps
        :param venue_url: url for get venue
        :type venue_url: str
        :return output_dictionary: dictionary data with all venue of the team
        :rtype output_dictionary: dict or None
    """
    # variables
    output_dictionary = dict()
    bf_html_content = get_beautiful_soup(venue_url)

    # tbl_map = bf_html_content.find_all("a", {"class": "google-maps-link"})
    tbl_map = bf_html_content.find_all("div", {"class": "block_venue_map"})
    if len(tbl_map) > 0:
        link = tbl_map[0].find("iframe")["src"]
        coordinates = link[link.index("&center=") + 8: link.index("&key=")].replace(" ", "")
        output_dictionary["coordinates"] = coordinates
        output_dictionary["map_link"] = "https://www.google.com/maps/@" + coordinates + ",15z"

    # tbl_content = bf_html_content.find_all("div", {"class": "block_venue_info"})
    tbl_content = bf_html_content.find_all("div", {"class": "block_venue_info"})
    if len(tbl_content) > 0:
        dl = tbl_content[0]

        # keys of the dict
        dt_list = dl.find_all("dt")
        dt_content_list = [str(e)[4:-5] for e in dt_list]
        # values of the dict
        dd_list = dl.find_all("dd")
        dd_content_list = [str(e)[4:-5] for e in dd_list]

        # replace unexpected characters
        for content_list in [dd_content_list, dt_content_list]:
            for index in range(len(content_list)):
                content_list[index] = content_list[index].replace("  ", "")
                content_list[index] = content_list[index].replace("\n", "")
                content_list[index] = content_list[index].replace("<br/>", ", ")

        for index in range(len(dd_content_list)):
            output_dictionary[dt_content_list[index]] = dd_content_list[index]

    return output_dictionary if len(output_dictionary.keys()) > 0 else None


def get_team_data_trophies(trophies_url):
    """
    Getter which allows to obtain a dictionary with the information of a team:
        - all club trophies since its creation at national level, classified by leagues
        - all club trophies since its creation at the international level, classified by leagues
        :param trophies_url: url for get trophies
        :type trophies_url: str
        :return output_dictionary: dictionary data with all trophies of the team
        :rtype output_dictionary: dict or None
    """
    # variables
    output_list = list()
    temp_dict = dict()
    league_node = None

    bf_html_content = get_beautiful_soup(trophies_url)
    tbl = bf_html_content.find_all("table", {"class": "trophies-table"})

    if len(tbl) > 0:
        # column name
        is_national = None
        tbl = tbl[0].find_all("tr")
        # print(tbl)
        for row in tbl:
            # if the row is the precision national/international
            if row.has_attr("class"):
                # print(row.find("th").text)
                is_national = 'omestic' in row.find("th").text
            elif is_national is not None:
                # by league
                if league_node is None or len(row.find_all("td", {"class": "competition"})) > 0:
                    league_node = row.find_all("td", {"class": "competition"})[0]

                    # print(row.find_all("td", {"class": "competition"}))
                    # print("~~~~~~")

                    # league
                    if len(league_node.find_all("a")) > 0:
                        if not len(temp_dict.keys()) == 0:
                            output_list.append(temp_dict)
                        temp_dict = dict()
                        league_dict = dict()
                        league_dict["name"] = league_node.find_all("a")[0].text.replace("  ", "").replace("\n", "")
                        league_dict["link"] = "https://int.soccerway.com" + league_node.find_all("a")[0]["href"]
                        league_dict["is_national"] = is_national
                        temp_dict["league"] = league_dict

                # win type
                try:
                    win_type_node = row.find_all("td", {"class": "label"})[0] if len(
                        row.find_all("td", {"class": "label"})) > 0 else None
                    if win_type_node is not None:
                        win_type_dict = dict()
                        win_type = win_type_node.text.lower()
                        win_type_dict["total"] = row.find_all("td", {"class": "total"})[0].text[:-1]
                        win_type_dict["seasons"] = []
                        try:
                            for season in row.find_all("td", {"class": "seasons"})[0].find_all("a"):
                                win_type_dict["seasons"].append(season.text)
                        except:
                            pass
                        try:
                            for season in row.find_all("td", {"class": "seasons"})[0].find_all("span"):
                                win_type_dict["seasons"].append(season.text)
                        except:
                            pass

                        temp_dict[win_type] = win_type_dict
                except:
                    pass

    return output_list if len(output_list) > 0 else None


def get_team_data_matches(matches_url):
    """
    Getter which allows to obtain a dictionary with the information of a team:
        - all the matches available with:
            the day,
            the date,
            the code of the league,
            the name of the league,
            the team 1,
            the team 2,
            the score,
            the link to have additional information on the match
        :param matches_url: url for get matches
        :type matches_url: str
        :return output_list: list data with all matches of the team
        :rtype output_list: list or None
    """
    # variables
    bf_html_content = get_beautiful_soup(matches_url)
    tbl = bf_html_content.find_all("div", {"class": "table-container"})[0]
    tbl = tbl.find_all("table", {"class": "matches"})[0]
    tbl_body = tbl.find_all("tbody")[0]

    output_list = []
    temp_dictionary = dict()

    for tr in tbl_body.find_all("tr"):
        try:
            tds = tr.find_all("td")
            temp_dictionary['day'] = tds[0].text
            temp_dictionary['date'] = tds[1].text
            # competition
            a_element = tds[2].find_all('a')[0]
            temp_dictionary['competition'] = {'title': a_element['title'], 'acronym': a_element.text}
            # team a
            a_element = tds[3].find_all('a')[0]
            code = a_element['href'][::-1][1:]
            code = code[:code.index('/')]
            temp_dictionary['team-a'] = {'code': code, 'name': a_element.text.replace("\n", "").lstrip().rstrip()}
            # result match
            a_element = tds[4].find_all('a')[0]
            statut = a_element['class'][0]
            score = a_element.text.replace("\n", "").replace("E", "").replace("P", "").lstrip().rstrip()
            temp_dictionary['result'] = {'statut': statut, 'score-a': score[0], 'score-b': score[len(score) - 1]}
            # team b
            a_element = tds[5].find_all('a')[0]
            code = a_element['href'][::-1][1:]
            code = code[:code.index('/')]
            temp_dictionary['team-b'] = {'code': code, 'name': a_element.text.replace("\n", "").lstrip().rstrip()}
            # mor infos
            temp_dictionary['more'] = 'https://int.soccerway.com/' + tds[5].find_all('a')[0]['href']

            output_list.append(temp_dictionary)
        except:
            pass

    return output_list if len(output_list) > 0 else None


def get_team_data_squad(team_id, squad_url, squad_info):
    """
    Getter which allows to obtain a dictionary with the information of a team:
        - all the current team with:
            player number,
            player name,
            player id,
            player place currently
        - the coach:
            the name,
            the id
        :param team_id: id of the team
        :type team_id: str
        :param squad_url: url for get squad
        :type squad_url: str
        :return output_dictionary: dictionary data with all squad of the team
        :rtype output_dictionary: dict or None
    """
    # variables
    output_list = []
    temp_dictionary = dict()

    bf_html_content = get_beautiful_soup(squad_url)
    # print(squad_url)
    # print(squad_url)
    tbl = bf_html_content.find_all("div", {"class": "squad-container"})[0]
    tbl = tbl.find_all("tbody")[0]

    tds = tbl.find_all("td", {"class": "photo"})

    for td in tds:
        try:
            code = td.find_all("a")[0]['href']
            code = code[::-1][1:]
            code = code[:code.index('/')][::-1]
            temp_dictionary = {'code': code}

            player_parameters_dictionary = squad_info
            player_parameters_dictionary['idP'] = code
            # print(code, end=' ')
            player = Players()
            # player.set_parameters_dictionary()
            temp_dictionary['player'] = player.json_players(player_parameters_dictionary)

            output_list.append(temp_dictionary)

        except:
            pass

    return output_list if len(output_list) > 0 else None


def get_team_data_statistics(team_id, statistics_url):
    """
    Getter which allows to obtain a dictionary with the information of a team:
 
        :param team_id: id of the team
        :type team_id: str
        :param statistics_url: url for get statistics
        :type statistics_url: str
        :return output_dictionary: dictionary data with all statistics of the team
        :rtype output_dictionary: dict or None
    """
    # variables
    output_dictionary = dict()
    bf_html_content = get_beautiful_soup(statistics_url)

    return output_dictionary if len(output_dictionary.keys()) > 0 else None


def get_team_data_fan_sites(team_id, fan_sites_url):
    """
    Getter which allows to obtain a dictionary with the information of a team:
 
        :param team_id: id of the team
        :type team_id: str
        :param fan_sites_url: url for get fan sites
        :type fan_sites_url: str
        :return output_list: list data with all fan sites of the team
        :rtype output_list: dict or None
    """
    # variables
    output_list = []
    temp_dictionary = dict()

    bf_html_content = get_beautiful_soup(fan_sites_url)

    tbl = bf_html_content.find_all("div", {"class": "block_team_fansites"})
    if len(tbl) == 0:
        return None
    tbl = tbl[0]

    # part logo of the club
    tbl_img = tbl.find_all("a")

    if len(tbl_img) > 0:
        for row in tbl_img:
            temp_dictionary["link"] = row["href"]
            temp_dictionary["name_site"] = row.text
            output_list.append(temp_dictionary)
            temp_dictionary = {}

    return output_list if len(output_list) > 0 else None


# ===============================================================
#   Other functions
# ===============================================================

def get_beautiful_soup(base_url):
    html_search = requests.get(base_url, headers=HEADERS).text
    soup_search = BeautifulSoup(html_search, features="lxml")
    return soup_search
