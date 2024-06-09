import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Load your OpenAI API key 
API_KEY = os.getenv('OPENAI_API_KEY')
print(f"Loaded API key: {API_KEY}")

# Ensure the API key is loaded correctly
if not API_KEY:
    raise ValueError("API key not found. Please set OPENAI_API_KEY in your .env file.")

# Set the headers and data for the request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 0.7
}

# Make the API request
response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)

# Print the response
print(response.status_code)
print(response.json())