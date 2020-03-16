from json import JSONDecodeError

import requests


def get_info(url, params=''):
    """
    get an object or a list of objects from an API.
    :param url: A url who returns a json object.
    :param params: search specific pages in the API
    :return: an object or a list of objects from an API.
    """
    if params is None:
        params = {}
    try:
        response = requests.get(url=url, params=params).json()
    except JSONDecodeError:
        return
    return response


class PlayerFeatureClass:
    """
    Makes an object of players from the NBA API
    """

    def __init__(self, search_type, search_param):
        """
        Gets a NBA player list according to a criteria from the api.
        :param search_type: 'id': according to id will find one player, 'name' to search for a name or part of a first/last
        name of players
        :param search_param: the parameter of search for id- a number for name a string.
        """
        if search_type == 'id':
            self.player = [get_info('https://www.balldontlie.io/api/v1/players/' + str(search_param))]
            if None in self.player:
                self.player = []
        elif search_type == 'name':
            self.player = get_info('https://www.balldontlie.io/api/v1/players/?search=' + search_param)['data']
        else:
            self.player = None

    def CheckID(self):
        """
        Returns the id of all players in the player list.
        :return: An id list of all players
        """
        return [i['id'] for i in self.player]

    def CheckName(self):
        """
        Returns all the names of the player list
        :return: return the names as items in a list [first_name,last_name]
        """
        return [[item['first_name'], item['last_name']] for item in self.player]

    def MetricUnits(self):
        """
        Translate a criteria in the player statics into metric.
        :return: A dictionary of translated units with player names as key.
        """
        imperial_to_metric = {'weight_pounds': 0.45359237, 'height_feet': 0.3048, 'height_inches': 0.0254}
        metric = {}
        for item in self.player:
            player_data = {}
            if item['weight_pounds'] is not None:
                player_data['weight'] = imperial_to_metric['weight_pounds'] * item['weight_pounds']
            else:
                player_data['weight'] = None
            if item['height_feet'] and item['height_inches'] is not None:
                player_data['height'] = imperial_to_metric['height_feet'] * item['height_feet'] + \
                                        imperial_to_metric['height_inches'] * item['height_inches']
            else:
                player_data['height'] = None

            metric[item['first_name'] + ' ' + item['last_name']] = player_data
        return metric
