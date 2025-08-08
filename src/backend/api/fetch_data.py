import requests
import os
from dotenv import load_dotenv
from backend.utils.logging import setup_logger

logger = setup_logger()

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")


# Define league & seasons
LEAGUE_ID = "1"
SEASON = "2023"


# API endpoint & headers


def fetch_teams(): 
    url = f"https://v1.american-football.api-sports.io/teams?league={LEAGUE_ID}&season={SEASON}"
    headers = {
    "x-rapidapi-host": "v1.american-football.api-sports.io",
    "x-rapidapi-key": API_KEY  # Use your actual API key
    }
    # Make request 
    response = requests.get(url, headers=headers)

    # Check if response was successful
    if response.status_code == 200:
        data = response.json()
        return data.get("response", [])

    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []
    
def fetch_players(team_id): 
    url = f"https://v1.american-football.api-sports.io/players?team={team_id}&season={SEASON}"
    headers = {
    "x-rapidapi-host": "v1.american-football.api-sports.io",
    "x-rapidapi-key": API_KEY  # Use your actual API key
    }
    # Make request 
    response = requests.get(url, headers=headers)

    # Check if response was successful
    if response.status_code == 200:
        data = response.json()
        return data.get("response", [])

    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []
    
def feth_season():
    url = f"https://v1.american-football.api-sports.io/seasons"
    headers = {
    "x-rapidapi-host": "v1.american-football.api-sports.io",
    "x-rapidapi-key": API_KEY  # Use your actual API key
    }

    # Make request
    response = requests.get(url, headers=headers)

    # Check if response was successful
    if response.status_code == 200:
        data = response.json()
        return data.get("response", [])
    
    else:
        logger.warning(f"Error: {response.status_code}, {response.text}")
        return []
    
def fetch_game_for_season(season):
    url = f"https://v1.american-football.api-sports.io/games?league=1&season={season}"
    headers = {
    "x-rapidapi-host": "v1.american-football.api-sports.io",
    "x-rapidapi-key": API_KEY  # Use your actual API key
    }

    # Make request
    response = requests.get(url, headers=headers)

    # Check if response was succesfull
    if response.status_code == 200:
        data = response.json()
        return data.get("response", [])
    else:
        logger.warning(f"Error: {response.status_code}, {response.text}")
        return []