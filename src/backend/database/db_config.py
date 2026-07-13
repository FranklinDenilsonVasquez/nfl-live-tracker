import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables
load_dotenv()

def get_db_config():
    return {
        'host': os.getenv('PGHOST'),
        'port': os.getenv('PGPORT', 5432),
        'user': os.getenv('PGUSER'),
        'password': os.getenv('PGPASSWORD'),
        'database': os.getenv('PGDATABASE')
    }
