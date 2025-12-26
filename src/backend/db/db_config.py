import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables
load_dotenv()

def get_db_config():
    return {
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT', 5432),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME')
    }
