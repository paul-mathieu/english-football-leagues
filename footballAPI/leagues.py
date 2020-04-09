# -*- coding: UTF-8 -*-

from .core import *
from bs4 import BeautifulSoup


class Leagues(object):

    def __init__(self, *args):
        pass

    def json_leagues(self, parameters_dictionary):
        self.set_parameters_dictionary_leagues(parameters_dictionary)
        self.set_URL_leagues()
        # self.display_leagues()
        # self.get_main_leagues()
        #self.get_all_leagues()
        #self.get_leagues_propre()
        self.get_leagues_propres_with_type()

    def set_parameters_dictionary_leagues(self, parameters_dictionary):
        self.parameters_dictionary = parameters_dictionary
        # print("test")

    def set_URL_leagues(self):
        # self.URL = BASE_URL + LEAGUES_START_URL + \
        #            "/" + self.parameters_dictionary["country"] + \
        #            "/" + self.parameters_dictionary["league"] + \
        #            "/" + self.get_year() + \
        #            LEAGUES_END_URL
        self.URL = BASE_URL +"/competitions/"

    def get_year(self):
        if "start year" in self.parameters_dictionary.keys():
            year = int(self.parameters_dictionary["start year"])
            return str(year) + str(year + 1)
        elif "end year" in self.parameters_dictionary.keys():
            year = int(self.parameters_dictionary["end year"])
            return str(year - 1) + str(year)
        else:
            return str(THIS_YEAR - 1) + str(THIS_YEAR)

    def display_leagues(self):
        print("url :", self.URL)
        print(get_HTML(self.URL))

    def get_main_leagues(self):
        """
        return a json object of the main english football leagues
        :return: json_object
        """
        html = get_HTML(self.URL)
        html_soup = BeautifulSoup(html, 'html.parser')
        liste = html_soup.find('ul', class_='left-tree')
        data_set = {"main_leagues": []}
        for url in liste.find_all('li'):
            if url['class'] == ['odd'] or url['class'] == ['even'] or url['class'] == ['expanded', 'odd'] or url[
                'class'] == ['expanded', 'even']:
                data_set['main_leagues'].append(url.a.string)

        # create json object
        json_dump = json.dumps(data_set)
        json_object = json.loads(json_dump)
        return json_object
        # je n'ai que les nom des leagues principales mais je n'ai pas les sous leagues de ces leagues.
        # pour cela il faut faire une requete pour chaque lien, pour qu'il me donne sa sous league.
        # remarque, il des fausses leagues parmi les leagues : Non League premier et Non League Div One
        # normalement y a 80 main leagues
        # result:
        # {'main_leagues': ['Premier League', 'Championship', 'League One', 'League Two', 'National League', 'National League N / S', 'Non League Premier', 'Non League Div One', 'North West Counties League Premier', 'FA Cup', 'League Cup', 'Community Shield', 'EFL Trophy', 'FA Trophy', 'FA Vase', 'Alan Turvey Trophy', 'Southern League Cup', 'Northern Premier League Challenge Cup', 'BBFA Senior Cup', 'Bedfordshire Senior Challenge Cup', 'Birmingham Senior Cup', 'Cheshire Senior Cup', 'Cumberland Senior Cup', 'Derbyshire Senior Cup', 'Durham County Challenge Cup', 'Gloucester Senior Challenge Cup', 'Huntingdonshire Senior Cup', 'Essex Senior Cup', 'East Riding Senior Cup', 'Hertfordshire Senior Challenge Cup', 'Kent Senior Cup', 'Lancashire FA Challenge Trophy', 'Lancashire Senior Cup', 'Lincolnshire Senior Cup', 'Liverpool Senior Cup', 'Leicestershire and Rutland Challenge Cup', 'London Senior Cup', 'Manchester Premier Cup', 'Manchester Senior Cup', 'Norfolk Senior Cup', 'Middlesex Senior Cup', 'North Riding Senior Cup', 'Northamptonshire Senior Cup', 'Northumberland Senior Cup', 'Nottinghamshire Saturday Senior Cup', 'Oxfordshire Senior Cup', 'Staffordshire Senior Cup', 'Sheffield and Hallamshire Senior Cup', 'Somerset Premier Cup', 'Suffolk FA Premier Cup', 'Surrey Senior Cup', 'Sussex Senior Challenge Cup', 'Walsall Senior Cup', 'West Riding County Cup', 'Central League', 'Central League Cup', 'Premier League 2 Division One', 'Premier League 2 Division Two', 'Professional Development League', 'Premier League Cup', 'U18 Premier League', 'FA Youth Cup', 'U18 Professional Development League', 'U18 Premier League Cup', 'Youth Alliance', 'Youth Alliance Cup', "Women's Super League", "Women's Championship", "Women's National League - Premier Division", "Women's National League - Division One", "FA Women's Cup", 'WSL Cup', 'U21 Premier League Division 1', 'U21 Premier League Division 2 ', 'Premier Reserve League', 'Conference League Cup', "Women's Premier League", "Women's League Cup", "Women's Play-offs 3/4", 'Club Friendlies']}
        #
        # REMARQUE: j'ai traite par classe car des fois les url n'ont pas de titre

    def get_all_leagues(self):
        """
        return all the english football leagues, even sub leagues
        :return: json_object
        """
        html = get_HTML(self.URL)
        html_soup = BeautifulSoup(html, 'html.parser')
        liste = html_soup.find('ul', class_='left-tree')
        data_set = {}
        for url in liste.find_all('li'):
            main_league = url.a.string
            print(main_league)
            if url['class'] == ['odd'] or url['class'] == ['even'] or url['class'] == ['expanded', 'odd'] or url['class'] == ['expanded', 'even']:
                new_url = BASE_URL + url.a['href']
                # we do that to get the sub leagues of each curent main leauges
                # which are only available if the current main leagues is selected (clicked)
                new_html = get_HTML(new_url)
                new_html_soup = BeautifulSoup(new_html, 'html.parser')
                data_set[main_league] = []
                listoflink = new_html_soup.select('ul.left-tree > li.expanded')[0].find_all('a')
                # if class = expanded, it's the current selected
                if len(listoflink) > 2: # we start at 2 to avoid the main leagues and the year in url <a>
                    for i in range(2, len(listoflink)):
                        data_set[main_league].append(listoflink[i].string)

        # create json object
        json_dump = json.dumps(data_set)
        json_object = json.loads(json_dump)
        return json_object

    def get_leagues_propre(self):
        """
        return a json object of the main english football leagues
        :return: json_object
        """
        # ex of result : {'leagues in england': [{'league name ': 'Premier League'}, {'league name ': 'Championship'},{'league name ': 'League Cup'}]}

        #https://int.soccerway.com/competitions/
        country = "england"
        html = get_HTML(self.URL)
        html_soup = BeautifulSoup(html, 'html.parser')
        country_soup = None
        data_set_names = "leagues in "+country
        data_set = {data_set_names: []}
        for list in html_soup.find_all('li', class_='expandable'):
            #print(list.find('a')['href'])
            link = list.find('a')['href']
            link1 = link.split('/')
            if country in link1:
                country_soup = list
                break # we stop here

        if country_soup is not None:
            area_id = country_soup['data-area_id']
            url_hidden_content = "https://int.soccerway.com/a/block_competitions_index_club_domestic?block_id=page_competitions_1_block_competitions_index_club_domestic_4&callback_params=%7B%22level%22:1%7D&action=expandItem&params=%7B%22area_id%22:%22" + area_id +"%22,%22level%22:2,%22item_key%22:%22area_id%22%7D"
            #  url_hidden_content is the url of the get method used by the website

            html_country_leagues = requests.get(url_hidden_content).json()["commands"][0]["parameters"]["content"] # convert the result into json
            country_league_soup = BeautifulSoup(html_country_leagues, 'html.parser')
            for link in country_league_soup.find_all('a'):
                data_set[data_set_names].append({'league name ': link.string})
                #print(link.string)
            #print(country_league_soup)

        # create json object
        json_dump = json.dumps(data_set)
        json_object = json.loads(json_dump)
        print(json_object)
        return json_object

    def get_leagues_propres_with_type(self):
        """
        return a json object of the main english football competitions with their type (ex: Domestic league, Domestic cup)
        :return:
        """
        country = "england"
        html = get_HTML(self.URL)
        html_soup = BeautifulSoup(html, 'html.parser')
        country_soup = None
        data_set_names = "leagues in " + country
        data_set = {data_set_names: []}
        for list in html_soup.find_all('li', class_='expandable'):
            link = list.find('a')['href']
            link1 = link.split('/')
            if country in link1:
                country_soup = list
                break  # we stop here

        if country_soup is not None:
            area_id = country_soup['data-area_id']
            url_hidden_content = "https://int.soccerway.com/a/block_competitions_index_club_domestic?block_id=page_competitions_1_block_competitions_index_club_domestic_4&callback_params=%7B%22level%22:1%7D&action=expandItem&params=%7B%22area_id%22:%22" + area_id + "%22,%22level%22:2,%22item_key%22:%22area_id%22%7D"
            #  url_hidden_content is the url of the get method used by the website

            html_country_leagues = requests.get(url_hidden_content).json()["commands"][0]["parameters"][
                "content"]  # convert the result into json
            country_league_soup = BeautifulSoup(html_country_leagues, 'html.parser')
            for row in country_league_soup.find_all('div', class_="row"):
                data_set[data_set_names].append({'competition name ': row.find('a').string, 'competition type ': row.find('span', class_="type").string})


        # create json object
        json_dump = json.dumps(data_set)
        json_object = json.loads(json_dump)
        print(json_object)
        return json_object
