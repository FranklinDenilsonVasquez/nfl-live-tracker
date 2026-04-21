from src.backend.database.db_connection import get_db_connection
from src.backend.utils.logging import logger
from src.backend.database.queries.game_queries import get_game_list, get_player_game_stats
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


def get_game_player_stats(game_id: int):
    conn = get_db_connection()

    if not conn:
        raise Exception("Database connection failed")
    try:
        with conn.cursor() as cursor:
            player_stats = get_player_game_stats(cursor, game_id)

            if not player_stats:
                logger.warning(f"No player stats found for game: {game_id}")
                return {
                    "away_team": [],
                    "home_team": []
                }

            return player_stats

    finally:
        conn.close()
