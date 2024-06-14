from dotenv import load_dotenv
import os
from pymongo import MongoClient
import redis

# Load environment variables from the .env file
load_dotenv()

# MongoDB setup
mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
mongo_client = MongoClient(mongo_uri)
db = mongo_client['restaurant_data']  

# Redis setup
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, db=0)

# Access the environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')