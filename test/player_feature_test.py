import unittest
from unittest.mock import patch, Mock
from src.player_feature import PlayerFeatureClass, get_info


class PlayerFeatureTest(unittest.TestCase):
    @patch('src.player_feature.requests.get')
    def test_page(self, mock_player):
        """
        Testing a few elements from the player feature
        :param mock_player: An input from patch.
        """
        player =  {'id': 237, 'first_name': 'LeBron', 'height_feet': 6, 'height_inches': 8,
                  'last_name': 'James', 'position': 'F', 'team': {'id': 14, 'abbreviation': 'LAL',
                                                                  'city': 'Los Angeles', 'conference': 'West',
                                                                  'division': 'Pacific',
                                                                  'full_name': 'Los Angeles Lakers',
                                                                  'name': 'Lakers'}, 'weight_pounds': 250}

        mock_player.return_value = Mock(ok=True)
        mock_player.return_value.json.return_value = player  # setting the API to only return this mock object.

        player2 = PlayerFeatureClass('id', player['id'])
        # expected
        expected_id = player['id']
        expected_id_type = list
        expected_first_name = player['first_name']
        expected_last_name = player['last_name']
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
                               delta=0.1)  # testing if the conversion is right.
        self.assertAlmostEqual(result4['LeBron James']['height'], expected_height_in_meters,
                               delta=0.1)  # testing if the conversion is right.

    if __name__ == '__main__':
        unittest.main()
