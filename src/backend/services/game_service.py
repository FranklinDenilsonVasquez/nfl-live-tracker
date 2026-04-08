from src.backend.database.db_connection import get_db_connection
from src.backend.utils.logging import logger
from src.backend.database.queries.game_queries import get_game_list
from pprint import pprint

def get_games_list(week: str, season: int, stage: str):
    conn = get_db_connection()

    if not conn:
        raise Exception("Failed to connect to database")
    try:
        with conn.cursor() as cursor:
            game_list = get_game_list(cursor, week, season, stage)

            if not game_list:
                logger.warning(f"No game data found")
                return []

            pprint(game_list, sort_dicts=False)

            return game_list
    finally:
        conn.close()

