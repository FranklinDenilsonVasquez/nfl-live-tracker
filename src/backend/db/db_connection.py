from dotenv import load_dotenv
from backend.db.db_config import get_db_config
import mysql.connector

# Load enviornment variables from .env file
load_dotenv()

# Access them


def get_db_connection():
    try:
        db_config = get_db_config()
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
