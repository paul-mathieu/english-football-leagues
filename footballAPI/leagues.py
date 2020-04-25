# -*- coding: UTF-8 -*-

from .core import *
from bs4 import BeautifulSoup


class Leagues(object):

    # ===============================================================
    #   Initialisation
    # ===============================================================

    def __init__(self, *args):
        self.parameters_dictionary = None
        self.URL = None
        self.request = None

    def json_leagues(self, parameters_dictionary):
        self.set_parameters_dictionary_leagues(parameters_dictionary)
        self.set_URL_leagues()
        self.process()
        self.get_player_with_market_value_of_a_team("manchester united", 2019)

    # ===============================================================
    #   Setters
    # ===============================================================

    def set_parameters_dictionary_leagues(self, parameters_dictionary):
        """
        Set the query option dictionary
        :param parameters_dictionary: dictionary of values
        :type parameters_dictionary: dict
        """
        self.parameters_dictionary = parameters_dictionary

    def set_URL_leagues(self):
        """
        Add the attribute URL
        """
        list_parameter_key = self.parameters_dictionary.keys()
        if "country" in list_parameter_key:
            if "league" in list_parameter_key:
                if "winner" in list_parameter_key and "end year" in list_parameter_key:
                    self.URL = BASE_URL + LEAGUES_START_URL + \
                               "/" + self.parameters_dictionary["country"] + \
                               "/" + self.parameters_dictionary["league"] + \
                               "/archive/"
                    self.request = 1
            elif "all" in list_parameter_key:
                self.URL = BASE_URL + LEAGUES_START_URL + \
                           "/" + self.parameters_dictionary["country"] + \
                           "/premier-league/"
                self.request = 2
            elif "type" in list_parameter_key:
                self.URL = BASE_URL + "/competitions/"
                self.request = 3
            else:
                self.URL = BASE_URL + "/competitions/"
                self.request = 4

    # ===============================================================
    #   Methods
    # ===============================================================

    def process(self):
        """
        run the right request depending on the request number stored in self.request
        """
        request = self.request
        if request == 1:
            self.get_winner()
        elif request == 2:
            self.get_all_leagues()
        elif request == 3:
            self.get_leagues_propres_with_type()
        elif request == 4:
            self.get_leagues_propre()

    def get_all_leagues(self):
        """
        Return all the english football leagues, even sub leagues
        :return json_object: data about leagues
        :rtype json_object: json
        """
        html = get_HTML(self.URL)
        html_soup = BeautifulSoup(html, 'html.parser')
        liste = html_soup.find('ul', class_='left-tree')
        data_set = {}
        for url in liste.find_all('li'):
            main_league = url.a.string
            if url['class'] == ['odd'] or url['class'] == ['even'] or url['class'] == ['expanded', 'odd'] or url[
                'class'] == ['expanded', 'even']:
                new_url = BASE_URL + url.a['href']
                # we do that to get the sub leagues of each current main leagues
                # which are only available if the current main leagues is selected (clicked)
                new_html = get_HTML(new_url)
                new_html_soup = BeautifulSoup(new_html, 'html.parser')
                data_set[main_league] = []
                listoflink = new_html_soup.select('ul.left-tree > li.expanded')[0].find_all('a')
                # if class = expanded, it's the current selected
                if len(listoflink) > 2:  # we start at 2 to avoid the main leagues and the year in url <a>
                    for i in range(2, len(listoflink)):
                        data_set[main_league].append(listoflink[i].string)

        # create json object
        json_dump = json.dumps(data_set)
        json_object = json.loads(json_dump)
        print(json_object)
        return json_object

    def get_leagues_propre(self):
        """
        return a json object of the main english football leagues
        :return json_object: data about leagues
        :rtype json_object: json
        """
        # ex of result : {'leagues in england': [{'league name ': 'Premier League'}, {'league name ':
        # 'Championship'},{'league name ': 'League Cup'}]}

        # https://int.soccerway.com/competitions/
        country = "england"
        html = get_HTML(self.URL)
        html_soup = BeautifulSoup(html, 'html.parser')
        country_soup = None
        data_set_names = "leagues in " + country
        data_set = {data_set_names: []}
        for list_element in html_soup.find_all('li', class_='expandable'):
            # print(list.find('a')['href'])
            link = list_element.find('a')['href']
            link1 = link.split('/')
            if country in link1:
                country_soup = list_element
                break  # we stop here

        if country_soup is not None:
            area_id = country_soup['data-area_id']
            url_hidden_content = "https://int.soccerway.com/a/block_competitions_index_club_domestic?block_id" \
                                 "=page_competitions_1_block_competitions_index_club_domestic_4&callback_params=%7B" \
                                 "%22level%22:1%7D&action=expandItem&params=%7B%22area_id%22:%22" + area_id + "%22," \
                                                                                                              "%22level%22:2,%22item_key%22:%22area_id%22%7D "
            #  url_hidden_content is the url of the get method used by the website

            html_country_leagues = requests.get(url_hidden_content).json()["commands"][0]["parameters"][
                "content"]  # convert the result into json
            country_league_soup = BeautifulSoup(html_country_leagues, 'html.parser')
            for link in country_league_soup.find_all('a'):
                data_set[data_set_names].append({'league name ': link.string})
                # print(link.string)
            # print(country_league_soup)

        # create json object
        json_dump = json.dumps(data_set)
        json_object = json.loads(json_dump)
        print(json_object)
        return json_object

    def get_leagues_propres_with_type(self):
        """
        Return a json object of the main english football competitions with their type (ex: Domestic league,
        Domestic cup) :return json_object: data about leagues
        :rtype json_object: json
        """
        country = self.parameters_dictionary["country"]
        html = get_HTML(self.URL)
        html_soup = BeautifulSoup(html, 'html.parser')
        country_soup = None
        data_set_names = "leagues in " + country
        data_set = {data_set_names: []}
        for list_element in html_soup.find_all('li', class_='expandable'):
            link = list_element.find('a')['href']
            link1 = link.split('/')
            if country in link1:
                country_soup = list_element
                break  # we stop here

        if country_soup is not None:
            area_id = country_soup['data-area_id']
            url_hidden_content = "https://int.soccerway.com/a/block_competitions_index_club_domestic?block_id" \
                                 "=page_competitions_1_block_competitions_index_club_domestic_4&callback_params=%7B" \
                                 "%22level%22:1%7D&action=expandItem&params=%7B%22area_id%22:%22" + area_id + "%22," \
                                                                                                              "%22level%22:2,%22item_key%22:%22area_id%22%7D "
            #  url_hidden_content is the url of the get method used by the website

            html_country_leagues = requests.get(url_hidden_content).json()["commands"][0]["parameters"][
                "content"]  # convert the result into json
            country_league_soup = BeautifulSoup(html_country_leagues, 'html.parser')
            for row in country_league_soup.find_all('div', class_="row"):
                data_set[data_set_names].append({'competition name ': row.find('a').string,
                                                 'competition type ': row.find('span', class_="type").string})

        # create json object
        json_dump = json.dumps(data_set)
        json_object = json.loads(json_dump)
        print(json_object)
        return json_object

        # avoir le gagnant d'une competition en ou de tou (les pr

    def get_winner(self):
        """
        return a json object of the winner of the competition which ended in end_year or all the winner of the
        competition through years with end_year="all"
        :return: json object
        """
        end_year = self.parameters_dictionary['end year']
        html = get_HTML(self.URL)
        html_soup = BeautifulSoup(html, 'html.parser')
        data_set_names = "winner of " + self.parameters_dictionary['league']
        data_set = {data_set_names: []}
        table_content = html_soup.find(id="page_competition_1_block_competition_archive_6-wrapper").find('table')
        # table which contains all the result
        if end_year != "all":  # we look for a winner for one season
            for row in table_content.find_all('tr')[1:]:  # we don't want the head of the table
                new_row = []  # new_row[0] -> season,  new_row[1] -> winner,
                for td in row.find_all('td'):
                    if td.find('a') is None:  # we do this way because sometimes we have <a> and sometime we don't,
                        # so we add content of td as a string in a list
                        element = td.string
                    else:
                        element = td.a.string
                    new_row.append(element)
                cleaned_season = (new_row[0].replace(" ", "").replace("\n", ""))  # we remove all the whitespaces
                # and line breaks
                cleaned_season_split = cleaned_season.split("/")
                if end_year == int(cleaned_season_split[1]):  # compare the end_year we provided and the end of
                    # current season if they match
                    json_row = {'season': cleaned_season, 'winner': new_row[1]}
                    data_set[data_set_names].append(json_row)
                    break  # we stop here because we've found what we were looking for

        else:  # we look for winners for all the season
            for row in table_content.find_all('tr')[1:]:  # we don't want the head of the table
                new_row = []  # new_row[0] -> season,  new_row[1] -> winner,
                for td in row.find_all('td'):
                    if td.find('a') is None:  # we do this way because sometimes we have and sometime we don't,
                        # so we add content of td as a string in a list
                        element = td.string
                    else:
                        element = td.a.string
                    new_row.append(element)
                cleaned_season = (new_row[0].replace(" ", "").replace("\n", ""))  # we remove all the whitespaces
                # and line breaks
                json_row = {'season': cleaned_season, 'winner': new_row[1]}
                data_set[data_set_names].append(json_row)

        # create json object
        json_dump = json.dumps(data_set)
        json_object = json.loads(json_dump)
        print(json_object)
        return json_object

    # ===============================================================
    #   Transfermarkt
    # ===============================================================

    def get_team_info(self, team):
        # WARNING : works only for premier league club for the moment
        # we do this way because we don't know how transfermarkt spells club name so we look for it by using the
        # search bar, and among the result we look for the one which best fits with the team we are looking for ( it
        # has to be in Premier league) NB : we can't have two teams with the same name in Premier League

        # NB: when we use the search bar, we might have different type of result like result table of manager, club,
        # players, etc. So we have to make sure we take the club result table.

        # NB: there are two manchester on Premier league, so the user has to type the whole name like manchester
        # united or manchester city

        """
        return the page link of a premier league team page
        :param team : string, team name
        :return dict: {"url_team_name ": ..., "team_id":...}
        """
        # return example : /fc-burnley/startseite/verein/1132
        # maintenant on return : {"url_team_name ": fc-burnley, "team_id":1132}
        url = "https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query={}&x=0&y=0".format(team)
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, '
                                 'like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

        # we set a header so that the website will know we are a real user otherwise it will block the program

        html = requests.get(url, headers=headers)
        html_soup = BeautifulSoup(html.text, 'html.parser')
        clubs = html_soup.select("div.large-12 > div.box > div.table-header")
        club = None
        result = []
        for c in clubs:
            if "Clubs" in c.text.split(" "):  # we take the table result of club
                club = c.find_next("div")  # we take the next div because it's this one which contains all the info
        for row in club.find_all("table", {"class": "inline-table"}):
            hrefs = row.find_all("a")
            # hrefs is a list of <a>, the first element is the team name and the second element (if it s exist it's the
            # team division )
            if len(hrefs) == 2:
                if hrefs[1]['title'] == "Premier League":  # check if the division is Premier league
                    result.append(hrefs)
                    # return {"url_team_name": hrefs[0]['href'].split("/")[1], "team_id": hrefs[0]['id']}
                    # we return the first team we find because in Premier league all team names are unique

        if len(result) > 1:
            # if there is several clubs in Premier league which corresponds to the name the user entered (ex:
            # "manchester", they will be "manchester city" and "manchester united", we don't which one of them the
            # user is looking for
            print("please be more specific on your research")
            return None
        elif len(result) == 1:
            return {"url_team_name": result[0][0]['href'].split("/")[1], "team_id": result[0][0]['id']}
        else:
            return None

    def get_player_with_market_value_of_a_team(self, team, season):
        """
        return a json object of player of team given with the market value of each player
        :param team: String, team name
        :param season: int, the beginning year of the season
        :return: json object
        """
        team_info = self.get_team_info(team)

        url = "https://www.transfermarkt.com/" + team_info["url_team_name"] + "/kader/verein/" + team_info[
            "team_id"] + "/plus/1/galerie/0?saison_id=" + str(season)

        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, '
                                 'like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

        # we set a header so that the website will know we are a real user otherwise it will block the program

        html = requests.get(url, headers=headers)
        html_soup = BeautifulSoup(html.text, 'html.parser')

        data_set_name = "player market value of " + team + " in " + str(season)
        data_set = {data_set_name: []}

        players = html_soup.find("table", {"class": "items"}).tbody
        for row in players.find_all("tr", recursive=False):  # recursive=False means we see direct children not the
            # descendants
            player_id = row.find("a", {"class": "spielprofil_tooltip"})['id']
            player_name = row.find("a", {"class": "spielprofil_tooltip"}).string
            player_contract_expires = row.find_all("td", {"class": "zentriert"}, recursive=False)[7].string
            # we have to do this way because there are others tds with class "zentriert" but with no id or anything else
            # so we use the index
            player_market_value = row.find("td", {"class": "rechts hauptlink"}).text.replace("\xa0", "")
            # we got "\xa0" code in the td so we replace by ""

            data_set[data_set_name].append({"player_id": player_id,
                                            "player_name": player_name,
                                            "player_contract_expires": player_contract_expires,
                                            "player_market_value": player_market_value})

        # create json object
        json_dump = json.dumps(data_set)
        json_object = json.loads(json_dump)
        print(json_object)
        return json_object
