''' Страница упражнения - 216 '''

# 11-1 11-2
import unittest

from city_functions import city_functions

class CityCountyTest(unittest.TestCase):

    def test_city_country(self):
        result = city_functions('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')

    def test_city_country_popular(self):
        result = city_functions('santiago', 'chile', 5_000_000)
        self.assertEqual(result, 'Santiago, Chile - population 5000000')