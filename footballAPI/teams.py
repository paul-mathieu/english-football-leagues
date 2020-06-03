# -*- coding: UTF-8 -*-
from .teams_external_getters import *


class Teams(object):
    """
    utl type : https://uk.soccerway.com/national/england/league-one/20182019/regular-season/r48115/tables/
      -> https://uk.soccerway.com/national/[country]/[League]/[yearyear]/regular-season/tables
    """

    # ===============================================================
    #   Initialisation
    # ===============================================================

    def __init__(self, *args):
        self.parameters_dictionary = None
        self.URL = None
        # print('init')

    # ===============================================================
    #   Setters
    # ===============================================================

    def set_parameters_dictionary(self, parameters_dictionary):
        """
        Set the query option dictionary
            :param parameters_dictionary: dictionary of values
            :type parameters_dictionary: dict
        """
        self.parameters_dictionary = {"name-team": None, "max-result": None,
                                      "info": False, "venue": False, "trophies": False,
                                      "matches": False, "squad": False, "fan-sites": False,
                                      "info-squad": {"API-type": "players"}}
        # print("test")

    def set_url_teams(self):
        """
        Set the URL for the request
        """
        self.URL = BASE_URL + TEAMS_START_URL + \
                   "/" + self.parameters_dictionary["country"] + \
                   "/" + self.parameters_dictionary["league"] + \
                   "/" + get_year(self.parameters_dictionary) + \
                   TEAMS_END_URL
        print(self.URL)
        
    # ===============================================================
    #   Getters
    # ===============================================================

    def get_name_team(self):
        """
        Get the name of the team in the parameter dictionary
            :return: name of the team
            :rtype: str
        """
        return self.parameters_dictionary["name-team"] if "name-team" in self.parameters_dictionary.keys() else False

    def get_max_result(self):
        """
        Get the number of results wanted in the parameter dictionary
            :return: max number of results
            :rtype: int
        """
        return self.parameters_dictionary["max-result"] if "max-result" in self.parameters_dictionary.keys() else False

    def get_info(self):
        """
        Get the value of info (wanted or not) in the parameter dictionary
            :return: is the team infos wanted
            :rtype: bool
        """
        return self.parameters_dictionary["info"] if "info" in self.parameters_dictionary.keys() else False

    def get_venue(self):
        """
        Get the value of info (wanted or not) in the parameter dictionary
            :return: is the team venue infos wanted
            :rtype: bool
        """
        return self.parameters_dictionary["venue"] if "venue" in self.parameters_dictionary.keys() else False

    def get_trophies(self):
        """
        Get the value of info (wanted or not) in the parameter dictionary
            :return: is the team trophies infos wanted
            :rtype: bool
        """
        return self.parameters_dictionary["trophies"] if "trophies" in self.parameters_dictionary.keys() else False

    def get_matches(self):
        """
        Get the value of info (wanted or not) in the parameter dictionary
            :return: is the team matches wanted
            :rtype: bool
        """
        return self.parameters_dictionary["matches"] if "matches" in self.parameters_dictionary.keys() else False

    def get_squad(self):
        """
        Get the value of info (wanted or not) in the parameter dictionary
            :return: is the team squad wanted
            :rtype: bool
        """
        return self.parameters_dictionary["squad"] if "squad" in self.parameters_dictionary.keys() else False

    def get_squad_info(self):
        """
        Get the name of th team in the parameter dictionary
            :return: parameters dictionary of a player
            :rtype: dict
        """
        return self.parameters_dictionary["squad-info"] if "squad-info" in self.parameters_dictionary.keys() else None

    def get_fan_sites(self):
        """
        Get the value of info (wanted or not) in the parameter dictionary
            :return: is the fan sites infos wanted
            :rtype: bool
        """
        return self.parameters_dictionary["fan-sites"] if "fan-sites" in self.parameters_dictionary.keys() else False


    # ===============================================================
    #   Methods
    # ===============================================================

    def fill_parameters_dictionary(self, parameters_dictionary):
        """
        fill self.parameters_dictionary
            :param parameters_dictionary: dictionary of query parameters
        """
        for key in parameters_dictionary.keys():
            self.parameters_dictionary[key] = parameters_dictionary[key]

    # ===============================================================
    #   Output
    # ===============================================================

    def json_teams(self, parameters_dictionary):
        """
        Apply the query with parameters and return a dictionary (json)
            :param parameters_dictionary: dictionary of query parameters
            :type parameters_dictionary: dict
            :return json_data: json data
            :rtype json_data: list
        """
        self.set_parameters_dictionary(parameters_dictionary)
        self.fill_parameters_dictionary(self.parameters_dictionary)
        # self.set_url_teams()

        id_list = get_team_id("liverpool FC")
        if type(self.get_max_result()) == str:
            max_number_results = int(self.get_max_result())
        else:
            max_number_results = self.get_max_result()

        # if there no max result value, only the first result
        if max_number_results is None:
            return [get_team_data(id_list[0],
                                  self.get_info(),
                                  self.get_venue(),
                                  self.get_trophies(),
                                  self.get_matches(),
                                  self.get_squad(),
                                  self.get_squad_info(),
                                  self.get_fan_sites())]

        # if max result value is too big, return all results
        if len(id_list) <= max_number_results:
            return [get_team_data(id,
                                  self.get_info(),
                                  self.get_venue(),
                                  self.get_trophies(),
                                  self.get_matches(),
                                  self.get_squad(),
                                  self.get_squad_info(),
                                  self.get_fan_sites())
                    for id in id_list]

        # else return requested max result
        return [get_team_data(id_list[index],
                              self.get_info(),
                              self.get_venue(),
                              self.get_trophies(),
                              self.get_matches(),
                              self.get_squad(),
                              self.get_squad_info(),
                              self.get_fan_sites())
                for index in range(max_number_results)]

    # ===============================================================
    #   Prints and debugs
    # ===============================================================

    def display_teams(self):
        # print("URL: ", self.URL, sep="")

        rows = self.get_table_teams()
        # print(rows[0])

        # my_xml = str(rows[0])
        # print(my_xml)
        # print("my_xml: ", my_xml, sep="")

    def tests_api_teams(self):
        callback_params = {"season_id": "17429", "round_id": "53145", "outgroup": "", "competition_id": "8",
                           "new_design_callback": "1"}
        params = {"type": "competition_overunder_table"}
        url = 'https://uk.soccerway.com/a/block_competition_tables?' \
              'block_id=page_competition_1_block_competition_tables_6&' \
              'callback_params=' + str(callback_params) + '&' \
                                                          'action=changeTable&' \
                                                          'params=' + str(params)
        # for s in url:
        #     print("\"" if s == "'" else s, end="")
        # print(url)

    def tests(self, parameters_dictionary):
        self.set_parameters_dictionary(parameters_dictionary)
        self.display_teams()
