import unittest
from unittest.mock import patch
from src.game_feature import GameFeatureClass


class GameFeatureTest(unittest.TestCase):
    @patch('src.game_feature.GameFeatureClass')
    def test_page(self, mock_game):
        game = mock_game()

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
        stub3 = '?postseason[]=False'
        stub4 = 'home_team_score'
        stub5 = 'visitor_team_score'

        # expected
        expected_id = 47179
        expected_id_type = int
        expected_game_date_2016 = '2016-11-17'
        expected_game_time_2016 = '00:00:00.000Z'
        expected_game_dt_type = list
        expected_home_team_score = 126
        expected_visitor_team_score = 94

        # action
        result1 = GameFeatureClass.CheckID(stub1)
        result2 = GameFeatureClass.SeasonsInfo(stub2).split('T')
        result3 = GameFeatureClass.PostSeasonInfo(stub3)
        result4 = GameFeatureClass.ScoreInfo(stub4)
        result5 = GameFeatureClass.ScoreInfo(stub5)

        # assert
        self.assertEqual(result1, expected_id)
        self.assertIsInstance(result1, expected_id_type)
        self.assertEqual(result2[0], expected_game_date_2016)
        self.assertEqual(result2[1], expected_game_time_2016)
        self.assertIsInstance(result2, expected_game_dt_type)
        self.assertFalse(result3)
        self.assertEqual(result4, expected_home_team_score)
        self.assertEqual(result5, expected_visitor_team_score)
        self.assertGreater(result4, result5)


if __name__ == '__main__':
    unittest.main()
