# src/config.py
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')