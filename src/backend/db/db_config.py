import os
from dotenv import load_dotenv

# Load enviornment variables
load_dotenv()

def get_db_config():
    return {
        'host': os.getenv('DB_HOST'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME')
    }
