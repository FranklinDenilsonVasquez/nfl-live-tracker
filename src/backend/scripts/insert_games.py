from src.backend.api.fetch_data import fetch_game_for_season
from src.backend.database.inserts.insert_data import (process_and_insert_stats, insert_games)
from src.backend.utils.logging import setup_logger as logger
from src.backend.database.db_connection import get_db_connection
import time

def insert_game():
    # Insert Games and Stats for each game.
    season_year = 2024
    games = fetch_game_for_season(season_year)
    logger().info(f"Fetched {len(games)} games for season {season_year}.")
    insert_games(games)
    # for game in games:
    #     api_game_id = None
    #     try:
    #         api_game_id = game.get("game", {}).get("id")
    
    #         if not api_game_id:
    #             logger().warning(f"Skipping game with missing API id: {game}")
    #             continue
    
    #         process_and_insert_stats(api_game_id, season_year)
    #         time.sleep(10)
    #     except Exception as e:
    #         logger().warning(f"Failed to insert player stats for game_id = {api_game_id} in season {season_year}: {e}")
    time.sleep(5)






if __name__ == "__main__":
    insert_game()