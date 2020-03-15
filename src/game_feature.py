import requests


def get_info(url, params=None):
    if params is None:
        params = {}
    response = requests.get(url=url, params=params)
    # print(response.json())
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

# GameFeatureClass.get_info()
