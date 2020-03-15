import requests


def get_info(url, params=None):
    if params is None:
        params = {}
    response = requests.get(url=url, params=params)
    return response.json()


class GameFeatureClass:

    @staticmethod
    def CheckID(stub_id):
        params = {
            'page': 1,
            'per_page': 1,
        }
        return get_info('https://www.balldontlie.io/api/v1/games', params)['data'][0][stub_id]

    @staticmethod
    def SeasonsInfo(stub_season):
        params = {
            'page': 1,
            'per_page': 1,
        }
        url = 'https://www.balldontlie.io/api/v1/games' + f'{stub_season}'
        return get_info(url, params=params)['data'][0]['date']

    @staticmethod
    def PostSeasonInfo(stub_ps_bool):
        params = {
            'page': 1,
            'per_page': 20,
        }
        url = 'https://www.balldontlie.io/api/v1/games' + f'{stub_ps_bool}'
        info = get_info(url, params=params)['data']
        for status in info:
            if status['postseason'] is True:
                return True
        return False

    @staticmethod
    def ScoreInfo(stub_team_type):
        params = {
            'page': 1,
            'per_page': 1,
        }
        return get_info('https://www.balldontlie.io/api/v1/games', params)['data'][0][stub_team_type]
