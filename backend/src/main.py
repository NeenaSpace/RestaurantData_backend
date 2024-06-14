from google_places import get_nearby_restaurants
from data_processor import process_and_save_restaurant_data, analyze_and_structure_dietary_info

def main():
    location = '40.748817,-73.985428' 
    radius = 5000 

    nearby_restaurants = get_nearby_restaurants(location, radius)
    process_and_save_restaurant_data(nearby_restaurants)

if __name__ == '__main__':
    main()