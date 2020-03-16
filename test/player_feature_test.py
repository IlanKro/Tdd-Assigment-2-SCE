import unittest
from unittest.mock import patch, Mock
from src.player_feature import PlayerFeatureClass, get_info


class PlayerFeatureTest(unittest.TestCase):
    @patch('src.player_feature.PlayerFeatureClass')
    def test_page(self, MockPlayer):
        """

        :param MockPlayer:
        :return:
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
        player2 = PlayerFeatureClass('id', 237)
        # assume
        stub1 = 'weight_pounds'
        stub2 = 'height_feet'

        # expected
        expected_id = 237
        expected_id_type = list
        expected_first_name = 'LeBron'
        expected_last_name = 'James'
        expected_name_dt_type = list
        expected_weight_in_kilo = 113.4
        expected_height_in_meters = 1.83

        # action
        result1 = player2.CheckID()
        result2 = player2.CheckName()
        result3 = player2.MetricUnits(stub1)
        result4 = player2.MetricUnits(stub2)

        # assert
        self.assertEqual(result1[0],expected_id)
        self.assertIsInstance(result1,expected_id_type)
        self.assertEqual(result2[0][0],expected_first_name)
        self.assertEqual(result2[0][1],expected_last_name)
        self.assertIsInstance(result2,expected_name_dt_type)
        self.assertAlmostEqual(result3[0],expected_weight_in_kilo, places=3)
        self.assertAlmostEqual(result4[0],expected_height_in_meters, places=3)

    if __name__ == '__main__':
        unittest.main()
