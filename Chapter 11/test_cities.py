import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do city-country pairs like 'Santiago, Chile' work?"""
        formatted_location = city_country('santiago', 'chile')
        self.assertEqual(formatted_location, 'Santiago, Chile')
    
    def test_city_country_population(self):
        """Do city-country-population like 'Santiago, Chile - Population: 5000000' work?"""
        formatted_location = city_country('santiago', 'chile', '5000000')
        self.assertEqual(formatted_location, 'Santiago, Chile - Population: 5000000')

unittest.main()