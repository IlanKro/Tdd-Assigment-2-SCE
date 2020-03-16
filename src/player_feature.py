from json import JSONDecodeError

import requests


def get_info(url, params=''):
    if params is None:
        params = {}
    try:
        response = requests.get(url=url, params=params).json()
    except JSONDecodeError:
        return
    return response


class PlayerFeatureClass:

    def __init__(self, search_type, search_param):
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
        return [[item['first_name'], item['last_name']] for item in self.player]

    def MetricUnits(self, param):
        imperial_to_metric = {'weight_pounds': 0.45359237, 'height_feet': 0.3048}
        imperial = [item[param] for item in self.player]
        metric = []
        for item in imperial:
            if item is not None:
                metric.append(round(imperial_to_metric[param] * item, 2))
            else:
                metric.append(None)
        return metric

    # get_info('https://www.balldontlie.io/api/v1/players/',{'page': 2})


# print(requests.get(url='https://www.balldontlie.io/api/v1/players/1').json())
# print(get_info('https://www.balldontlie.io/api/v1/players/?search=Lebron'))
# hello = get_info('https://www.balldontlie.io/api/v1/players/237')
# print(len(hello))
# print(hello)
# print(PlayerFeatureClass.MetricUnits(237, 'weight_pounds'))
"""
LeBron = PlayerFeatureClass('name', 'LeB')
LeBron2 = PlayerFeatureClass('id', '237')
print(LeBron.player)
print(LeBron2.player)
print(LeBron.player == LeBron2.player)
print(LeBron.CheckID())
print(LeBron.CheckName())
print(LeBron.player)
print(LeBron.MetricUnits('weight_pounds'))
"""