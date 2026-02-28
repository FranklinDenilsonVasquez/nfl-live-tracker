from src.backend.api.fetch_data import fetch_player_stats as api_player_stats
from src.backend.database.services.player_game_stats_service import orchestrate_player_game_stats, process_player_game_stats
from src.backend.database.db_connection import get_db_connection
from src.backend.utils.logging import logger
from pprint import pprint

def ingest_player_game_stats(game_id:int):
    conn = get_db_connection()
    if not conn:
        logger.warning("Connection to database failed")
        return

    game_response = api_player_stats(game_id)

    if not game_response:
        logger.warning(f"No data found for player in game_id = {game_id}")
        return

    try:
        process_player_game_stats(conn, game_response, game_id)
    except Exception:
        logger.exception(f"Something went wrong during processing : {Exception}")
    finally:
        conn.close()



if __name__ == "__main__":
    ingest_player_game_stats(4000)
