import requests
import os
from dotenv import load_dotenv
from utils.logging import setup_logger

logger = setup_logger()

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")


# Define league & seasons
LEAGUE_ID = "1"
SEASON = "2023"


# API endpoint & headers

# Function to fetch all data from all pages that the API response gives


def fetch_teams(): 
    url = f"https://v1.american-football.api-sports.io/teams?league={LEAGUE_ID}&season={SEASON}"
    headers = {
    "x-rapidapi-host": "v1.american-football.api-sports.io",
    "x-rapidapi-key": API_KEY  
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
    
    
def fetch_players(team_id, season): 
    url = "https://v1.american-football.api-sports.io/players"
    params = {
        "team": team_id,
        "season": season
    }
    headers = {
        "x-rapidapi-host": "v1.american-football.api-sports.io",
        "x-rapidapi-key": API_KEY
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    players = data.get("response", [])
    
    if players:
        return players
    else:
        print(f"Error: No players found for team {team_id} in season {season}")
        return []
    
def fetch_season():
    url = f"https://v1.american-football.api-sports.io/seasons"
    headers = {
    "x-rapidapi-host": "v1.american-football.api-sports.io",
    "x-rapidapi-key": API_KEY  
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
    url = "https://v1.american-football.api-sports.io/games"
    params = {
        "league": 1,
        "season": season
    }
    headers = {
            "x-rapidapi-host": "v1.american-football.api-sports.io",
            "x-rapidapi-key": API_KEY  
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()
    games = data.get("response", [])

    if games:
        return games
    else:
        print(f"No games found for season {season}")
        return []
    
#def fetch_team_game_stats()


# Function to fetch player statistical data game by game
def fetch_player_stats(gameId):
    url = "https://v1.american-football.api-sports.io/games/statistics/players"
    params = {
        "id": gameId
    }

    headers = {
        "x-rapidapi-host": "v1.american-football.api-sports.io",
        "x-rapidapi-key": API_KEY  
    }
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()
    player_stats = data.get("response",[])

    if player_stats:
        return player_stats
    else:
        logger.warning(f"No player stats found for game")
        return []