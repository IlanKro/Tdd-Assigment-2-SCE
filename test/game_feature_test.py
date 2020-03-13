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

        # assume
        stub1 = 'id'

        # expected
        expected1 = 47179
        expected2 = int

        # action
        result1 = GameFeatureClass.CheckID(stub1)

        # assert
        self.assertEqual(result1, expected1)
        self.assertIsInstance(result1, expected2)


if __name__ == '__main__':
    unittest.main()
