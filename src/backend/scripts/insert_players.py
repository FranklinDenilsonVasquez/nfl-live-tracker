from src.backend.api.fetch_data import fetch_teams, fetch_season, fetch_game_for_season, fetch_player_stats, fetch_players
from src.backend.database.inserts.insert_data import (process_and_insert_stats, insert_players)
from src.backend.utils.logging import setup_logger
import time
from pprint import pprint

logger = setup_logger()

def insert_player():
    teams = fetch_teams() 
    # Insert players and coach team by team
    for season_year in range(2022, 2025):  # range(2022,2025) to run from 2022-2024 because of the free plan (API)
        logger.info(f"Processing season : {season_year}")
        for team in teams:
            team_id = team['id']
            team_name = team['name']
            try:
                players = fetch_players(team_id, season_year)
                player_length = len(players)
                logger.info(f"Fetched {len(players)} players for {team_name} (ID {team_id})")
                if player_length == 0:
                    logger.warning(f"Zero players for team: {team_name} (ID {team_id})")
    
                insert_players(players, team_id, season_year)
                #insert_coach_from_team(team, season_year)
                #logger.info(f"Finished adding coaches into database")
                time.sleep(7)
            except Exception as e:
                logger.warning(f"Failed to fetch players for {team_name} (ID {team_id}): {e}")
                #logger.warning(f"Failed to insert coach for {team_name} (ID {team_id}): {e}")

if __name__ == "__main__":
    insert_player()