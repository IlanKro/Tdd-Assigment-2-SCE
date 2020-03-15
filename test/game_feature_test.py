import unittest
from unittest.mock import patch
from src.game_feature import GameFeatureClass


class GameFeatureTest(unittest.TestCase):
    @patch('src.game_feature.GameFeatureClass')
    def test_page(self, MockGame):
        game = MockGame()

        game.data.return_value = {'data': [{'id': 47179, 'date': '2019-01-30T00:00:00.000Z',
                                            'home_team': {'id': 2, 'abbreviation': 'BOS', 'city': 'Boston',
                                                          'conference': 'East', 'division': 'Atlantic',
                                                          'full_name': 'Boston Celtics', 'name': 'Celtics'},
                                            'home_team_score': 126, 'period': 4, 'postseason': False, 'season': 2018,
                                            'status': 'Final', 'time': ' ',
                                            'visitor_team': {'id': 4, 'abbreviation': 'CHA', 'city': 'Charlotte',
                                                             'conference': 'East', 'division': 'Southeast',
                                                             'full_name': 'Charlotte Hornets', 'name': 'Hornets'},
                                            'visitor_team_score': 94}],
                                  'meta': {'total_pages': 48754, 'current_page': 1, 'next_page': 2, 'per_page': 1,
                                           'total_count': 48754}}

        game.twentysixteen.season.return_value = {'data': [{'id': 32809, 'date': '2016-11-17T00:00:00.000Z',
                                                            'home_team': {'id': 29, 'abbreviation': 'UTA',
                                                                          'city': 'Utah', 'conference': 'West',
                                                                          'division': 'Northwest',
                                                                          'full_name': 'Utah Jazz', 'name': 'Jazz'},
                                                            'home_team_score': 77, 'period': 4, 'postseason': False,
                                                            'season': 2016, 'status': 'Final', 'time': ' ',
                                                            'visitor_team': {'id': 5, 'abbreviation': 'CHI',
                                                                             'city': 'Chicago', 'conference': 'East',
                                                                             'division': 'Central',
                                                                             'full_name': 'Chicago Bulls',
                                                                             'name': 'Bulls'},
                                                            'visitor_team_score': 85}],
                                                  'meta': {'total_pages': 1309, 'current_page': 1, 'next_page': 2,
                                                           'per_page': 1, 'total_count': 1309}}

        # assume
        stub1 = 'id'
        stub2 = '?seasons[]=2016'

        # expected
        expected1 = 47179
        expected2 = int
        expected3 = '2016-11-17'
        expected4 = '00:00:00.000Z'

        # action
        result1 = GameFeatureClass.CheckID(stub1)
        result2 = GameFeatureClass.SeasonsInfo(stub2).split('T')

        # assert
        self.assertEqual(result1, expected1)
        self.assertIsInstance(result1, expected2)
        self.assertEqual(result2[0], expected3)
        self.assertEqual(result2[1], expected4)


if __name__ == '__main__':
    unittest.main()
