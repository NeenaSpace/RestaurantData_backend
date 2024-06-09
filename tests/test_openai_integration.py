import openai
from src.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def extract_dietary_info(reviews):
    combined_reviews = ' '.join([review['text'] for review in reviews])
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that extracts dietary information from text."},
            {"role": "user", "content": f"Extract dietary information from the following text: {combined_reviews}"}
        ],
        temperature=0.7,
        max_tokens=150
    )
    return response['choices'][0]['message']['content'].strip()