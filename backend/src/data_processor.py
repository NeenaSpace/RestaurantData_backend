# src/data_processor.py

from google_places import get_nearby_restaurants, get_restaurant_details
from openai_integration import extract_dietary_info, determine_primary_diet_type, is_restaurant
from config import db

def process_and_save_restaurant_data(location, radius, keyword=None):
    # 获取附近餐厅数据
    nearby_restaurants = get_nearby_restaurants(location, radius, keyword)
    print("Fetching nearby restaurants...")
    
    for restaurant in nearby_restaurants:
        try:
            print(f"Processing place: {restaurant['name']} with place_id: {restaurant['place_id']}")
            details = get_restaurant_details(restaurant['place_id'])
            print(f"Retrieved details for {restaurant['name']}")
            
            # 使用 OpenAI API 进一步验证是否为餐厅
            if 'reviews' in details and is_restaurant(details['reviews']):
                print(f"{restaurant['name']} is identified as a restaurant by OpenAI.")
                
                # 提取饮食信息
                dietary_info = extract_dietary_info(details.get('reviews', []))
                
                # 结构化数据
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
                
                # 将结构化数据插入MongoDB
                db.restaurants.insert_one(structured_info)
        except Exception as e:
            print(f"Error processing {restaurant['name']}: {e}")

def summarize_reviews(reviews):
    review_texts = [review['text'] for review in reviews[:3]]
    return ' '.join(review_texts)

def analyze_and_structure_dietary_info(restaurant_data):
    structured_info = {
        'Restaurant Name': restaurant_data['name'],
        'Address': restaurant_data['address'],
        'City': restaurant_data['address'].split(',')[-2].strip(),
        'Review Summary': summarize_reviews(restaurant_data['reviews']),
        'Diet Type': determine_primary_diet_type(restaurant_data['dietary_info']),
        'Diet Details': restaurant_data['dietary_info']
    }
    
    return structured_info