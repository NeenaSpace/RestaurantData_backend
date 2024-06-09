import os
import requests
from config import OPENAI_API_KEY

def extract_dietary_info(reviews):
    combined_reviews = ' '.join([review['text'] for review in reviews])
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant specialized in dietary information."},
            {"role": "user", "content": f"Extract dietary information from the following text, focusing on dietary preferences such as vegan, vegetarian, gluten-free, and other dietary restrictions: {combined_reviews}"}
        ],
        "max_tokens": 150
    }
    
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    response_json = response.json()
    return response_json['choices'][0]['message']['content'].strip()

def is_restaurant(reviews):
    combined_reviews = ' '.join([review['text'] for review in reviews])
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Based on the following text, is the place described a restaurant? Answer with 'Yes' or 'No': {combined_reviews}"}
        ],
        "max_tokens": 10
    }
    
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    response_json = response.json()
    return response_json['choices'][0]['message']['content'].strip().lower() == 'yes'