import sys
import os

from googlemaps import Client
from src.config import GOOGLE_API_KEY

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print(f"Adding {root_path} to PYTHONPATH")
sys.path.append(root_path)

print("Current PYTHONPATH:", sys.path)

API_KEY = os.getenv('GOOGLE_API_KEY')
print(f"Loaded API key: {API_KEY}")

def test_google_places_api():
    gmaps = Client(key=GOOGLE_API_KEY)
    location = '40.748817,-73.985428'  
    radius = 5000  

    places_result = gmaps.places_nearby(location=location, radius=radius, type='restaurant')
    print(places_result)

if __name__ == "__main__":
    test_google_places_api()