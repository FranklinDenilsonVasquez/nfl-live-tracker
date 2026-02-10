from dotenv import load_dotenv
from src.backend.database.db_config import get_db_config
import psycopg2
from psycopg2 import OperationalError

# Load environment variables from .env file
load_dotenv()

# Access them


def get_db_connection():
    try:
        db_config = get_db_config()
        conn = psycopg2.connect(**db_config)
        return conn
    except OperationalError as err:
        print(f"Error: {err}")
        return None
