# src/data_processor.py

from google_places import get_restaurant_details
from openai_integration import extract_dietary_info, is_restaurant
from config import db

def process_and_save_restaurant_data(restaurant_data):
    for restaurant in restaurant_data:
        details = get_restaurant_details(restaurant['place_id'])
        if is_restaurant(details.get('reviews', [])):
            dietary_info = extract_dietary_info(details.get('reviews', []))
            structured_info = analyze_and_structure_dietary_info({
                'name': restaurant['name'],
                'address': details.get('formatted_address'),
                'phone_number': details.get('formatted_phone_number'),
                'website': details.get('website'),
                'rating': details.get('rating'),
                'user_ratings_total': details.get('user_ratings_total'),
                'reviews': details.get('reviews'),
                'dietary_info': dietary_info,
                'types': details.get('types'),
                'business_status': details.get('business_status'),
                'opening_hours': details.get('opening_hours'),
                'price_level': details.get('price_level')
            })
            db.restaurants.insert_one(structured_info)

def summarize_reviews(reviews):
    review_texts = [review['text'] for review in reviews[:3]]  
    return ' '.join(review_texts)

def determine_diet_type(dietary_info):
    if 'vegan' in dietary_info.lower():
        return 'Vegan'
    if 'vegetarian' in dietary_info.lower():
        return 'Vegetarian'
    if 'gluten-free' in dietary_info.lower():
        return 'Gluten-free'
    return 'Unknown'

def analyze_and_structure_dietary_info(restaurant_data):
    structured_info = {
        'Restaurant Name': restaurant_data['name'],
        'Address': restaurant_data['address'],
        'City': restaurant_data['address'].split(',')[-2].strip(),
        'Review Summary': summarize_reviews(restaurant_data['reviews']),
        'Diet Type': determine_diet_type(restaurant_data['dietary_info']),
        'Diet Details': restaurant_data['dietary_info']
    }
    
    # Print structured information
    print("\nStructured Dietary Information:")
    print(f"Restaurant Name: {structured_info['Restaurant Name']}")
    print(f"Address: {structured_info['Address']}")
    print(f"City: {structured_info['City']}")
    print("Review Summary:")
    print(structured_info['Review Summary'])
    print("Diet Details:")
    print(structured_info['Diet Details'])
    
    return structured_info