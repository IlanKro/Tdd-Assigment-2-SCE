import requests


def get_info(url):
    """
    :param url: the api url request
    :return: json() info of the response
    """
    response = requests.get(url=url)
    return response.json()


class GameFeatureClass:

    @staticmethod
    def CheckID(param):
        """
        :param param: the key which will produce me the needed value
        :return: key's value
        """
        return get_info('https://www.balldontlie.io/api/v1/games')['data'][0][param]

    @staticmethod
    def SeasonsInfo(param):
        """
        :param param: the key which will produce me the needed value
        :return: key's value
        """
        return get_info('https://www.balldontlie.io/api/v1/games')['data'][0][param]

    @staticmethod
    def PostSeasonInfo(param):
        """
        :param param: the key which will produce me the needed value
        :return: key's value
        """
        url = 'https://www.balldontlie.io/api/v1/games'
        info = get_info(url)['data'][0]
        if info[param] is True:
            return True
        return False

    @staticmethod
    def ScoreInfo(param):
        """
        :param param: the key which will produce me the needed value
        :return: key's value
        """
        return get_info('https://www.balldontlie.io/api/v1/games')['data'][0][param]
