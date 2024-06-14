import googlemaps
import json
from config import redis_client
from config import GOOGLE_API_KEY

gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

def get_nearby_restaurants(location, radius, keyword=None):
    cache_key = f"restaurants:{location}:{radius}:{keyword}"
    cached_data = redis_client.get(cache_key)

    if cached_data:
        return json.loads(cached_data)

    places_result = gmaps.places_nearby(location=location, radius=radius, type='restaurant', keyword=keyword)
    restaurants = []
    for place in places_result['results']:
        if 'restaurant' in place.get('types', []):
            restaurant_info = {
                'name': place.get('name'),
                'address': place.get('vicinity'),
                'rating': place.get('rating'),
                'user_ratings_total': place.get('user_ratings_total'),
                'place_id': place.get('place_id'),
                'types': place.get('types'),
                'business_status': place.get('business_status'),
                'opening_hours': place.get('opening_hours'),
                'price_level': place.get('price_level')
            }
            restaurants.append(restaurant_info)
    
    redis_client.set(cache_key, json.dumps(restaurants), ex=3600)  # Cache for 1 hour
    return restaurants

# def get_nearby_restaurants(location, radius, keyword=None):
#     places_result = gmaps.places_nearby(location=location, radius=radius, type='restaurant', keyword=keyword)
#     restaurants = []
#     for place in places_result['results']:
#         if 'restaurant' in place.get('types', []):  # Ensure the place is a restaurant
#             restaurant_info = {
#                 'name': place.get('name'),
#                 'address': place.get('vicinity'),
#                 'rating': place.get('rating'),
#                 'user_ratings_total': place.get('user_ratings_total'),
#                 'place_id': place.get('place_id'),
#                 'types': place.get('types'),
#                 'business_status': place.get('business_status'),
#                 'opening_hours': place.get('opening_hours'),
#                 'price_level': place.get('price_level')
#             }
#             restaurants.append(restaurant_info)
#     return restaurants

def get_restaurant_details(place_id):
    place_details = gmaps.place(place_id=place_id)
    details = place_details['result']
    return {
        'name': details.get('name'),
        'formatted_address': details.get('formatted_address'),
        'phone_number': details.get('formatted_phone_number'),
        'website': details.get('website'),
        'rating': details.get('rating'),
        'user_ratings_total': details.get('user_ratings_total'),
        'reviews': details.get('reviews'),
        'types': details.get('types'),
        'business_status': details.get('business_status'),
        'opening_hours': details.get('opening_hours'),
        'price_level': details.get('price_level')
    }