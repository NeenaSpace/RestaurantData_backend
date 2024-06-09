from google_places import get_nearby_restaurants
from data_processor import process_and_save_place_data, analyze_and_structure_dietary_info



def main():
    location = '40.748817,-73.985428'  
    radius = 1000  
    nearby_places = get_nearby_restaurants(location, radius)
    for place in nearby_places:
        processed_data = process_and_save_place_data(place)
        if processed_data:
            analyze_and_structure_dietary_info(processed_data)

if __name__ == "__main__":
    main()