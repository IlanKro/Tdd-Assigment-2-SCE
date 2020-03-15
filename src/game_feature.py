import requests


def get_info(url):
    response = requests.get(url=url)
    return response.json()


class GameFeatureClass:

    @staticmethod
    def CheckID(param):
        return get_info('https://www.balldontlie.io/api/v1/games')['data'][0][param]

    @staticmethod
    def SeasonsInfo(param):
        return get_info('https://www.balldontlie.io/api/v1/games')['data'][0][param]

    @staticmethod
    def PostSeasonInfo(param):
        url = 'https://www.balldontlie.io/api/v1/games'
        info = get_info(url)['data'][0]
        if info[param] is True:
            return True
        return False

    @staticmethod
    def ScoreInfo(param):
        return get_info('https://www.balldontlie.io/api/v1/games')['data'][0][param]
