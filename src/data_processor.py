from google_places import get_restaurant_details
from openai_integration import extract_dietary_info, is_restaurant

def process_and_save_place_data(place):
    if 'restaurant' in place['types']:
        place_id = place['place_id']
        details = get_restaurant_details(place_id)
        
        if is_restaurant(details.get('reviews', [])):
            dietary_info = extract_dietary_info(details.get('reviews', []))
            diet_type = determine_diet_type(dietary_info)
            restaurant_data = {
                'name': details['name'],
                'address': details.get('formatted_address'),
                'city': details.get('formatted_address').split(',')[-2].strip(), 
                'review_summary': summarize_reviews(details.get('reviews', [])), 
                'diet_type': diet_type,
                'diet_details': dietary_info
            }
            return restaurant_data
    return None

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
        'City': restaurant_data['city'],
        'Review Summary': restaurant_data['review_summary'],
        'Diet Type': restaurant_data['diet_type'],
        'Diet Details': restaurant_data['diet_details']
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