# tests/test_google_places.py
import unittest
from src.google_places import get_nearby_restaurants, get_restaurant_details

class TestGooglePlaces(unittest.TestCase):
    def test_get_nearby_restaurants(self):
        location = '40.748817,-73.985428'
        radius = 5000
        result = get_nearby_restaurants(location, radius)
        self.assertTrue(len(result) > 0)

    def test_get_restaurant_details(self):
        place_id = 'ChIJN1t_tDeuEmsRUsoyG83frY4'  # Example place_id
        result = get_restaurant_details(place_id)
        self.assertIn('name', result)

if __name__ == '__main__':
    unittest.main()
