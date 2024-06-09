# src/test_env.py
from config import GOOGLE_API_KEY, OPENAI_API_KEY

def test_env_vars():
    print(f"Google API Key: {GOOGLE_API_KEY}")
    print(f"OpenAI API Key: {OPENAI_API_KEY}")

if __name__ == "__main__":
    test_env_vars()