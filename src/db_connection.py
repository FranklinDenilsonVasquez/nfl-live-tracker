from dotenv import load_dotenv
import os

# Load enviornment variables from .env file
load_dotenv()

# Access them
API_KEY = os.getenv("API_KEY")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

print(f"Connected to {DB_NAME} at {DB_HOST} with user {DB_USER}")
