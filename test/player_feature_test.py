import unittest
from unittest.mock import patch, Mock
from src.player_feature import PlayerFeatureClass, get_info


class PlayerFeatureTest(unittest.TestCase):
    @patch('src.player_feature.PlayerFeatureClass')
    def test_page(self, MockPlayer):
        """
        Testing a few elements from the player feature
        :param MockPlayer: An input from patch.
        """
        player = {'data': [{'id': 237, 'first_name': 'LeBron', 'height_feet': 6, 'height_inches': 8,
                            'last_name': 'James', 'position': 'F', 'team': {'id': 14, 'abbreviation': 'LAL',
                                                                            'city': 'Los Angeles', 'conference': 'West',
                                                                            'division': 'Pacific',
                                                                            'full_name': 'Los Angeles Lakers',
                                                                            'name': 'Lakers'},
                            'weight_pounds': 250}],
                  'meta': {'total_pages': 1, 'current_page': 1, 'next_page': None, 'per_page': 25, 'total_count': 1}}

        MockPlayer.return_value = Mock(ok=True)
        MockPlayer.return_value.json.return_value = player
        player2 = PlayerFeatureClass('id', player['data'][0]['id'])
        player3 = PlayerFeatureClass('name', player['data'][0]['first_name'])

        # expected
        expected_id = player['data'][0]['id']
        expected_id_type = list
        expected_first_name = player['data'][0]['first_name']
        expected_last_name = player['data'][0]['last_name']
        expected_name_dt_type = list
        expected_weight_in_kilo = 113.39
        expected_height_in_meters = 2.06

        # action
        result1 = player2.CheckID()
        result2 = player2.CheckName()
        result3 = player2.MetricUnits()
        result4 = player2.MetricUnits()

        # assert
        self.assertEqual(result1[0], expected_id)  # testing if the id is equal to the mock
        self.assertIsInstance(result1, expected_id_type)  # testing if the id is a list (although being a single number)
        self.assertEqual(result2[0][0], expected_first_name)  # testing if the name is the same.
        self.assertEqual(result2[0][1], expected_last_name)  # testing if the last name is the same.
        self.assertIsInstance(result2, expected_name_dt_type)  # testing if the give name is a list of names.
        self.assertAlmostEqual(result3['LeBron James']['weight'], expected_weight_in_kilo,
                               delta=0.1)  # testing if the convertion is right.
        self.assertAlmostEqual(result4['LeBron James']['height'], expected_height_in_meters,
                               delta=0.1)  # testing if the convertion is right.
        self.assertEqual(player2.player, player3.player)

    if __name__ == '__main__':
        unittest.main()
