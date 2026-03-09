from src.backend.api.fetch_data import fetch_player_stats as api_player_stats
from services import process_player_game_stats
from src.backend.database.db_connection import get_db_connection
from src.backend.api.fetch_data import fetch_game_for_season
from src.backend.scripts.utils.game_already_ingested import game_already_exists
from src.backend.utils.logging import logger
import time

def ingest_player_game_stats():
    conn = get_db_connection()
    cursor = conn.cursor()
    if not conn:
        logger.warning("Connection to database failed")
        return
    try:
        for year in range(2022,2023):
            logger.info(f"Processing season {year}")
            games = fetch_game_for_season(year)
            for game in games:
                game_id = None
                try:
                    game_id = game.get("game", {}).get("id")
                    if not game_id:
                        logger.warning(f"Skipping game with missing API id: {game}")
                        continue
                    if game_already_exists(cursor, game_id):
                        logger.info(f"Player stats for game = {game_id} already exists. "
                                    f"Skipping to avoid duplicate data ingestion")
                        continue

                    game_response = api_player_stats(game_id)

                    if not game_response:
                        logger.warning(f"No data found for player in game_id = {game_id}")
                        continue

                    process_player_game_stats(conn, game_response, game_id)
                    time.sleep(7)
                except Exception:
                    logger.exception(f"Failed processing game_id={game_id}")

    finally:
        conn.close()
        logger.info("Database connection closed")



if __name__ == "__main__":
    ingest_player_game_stats()
