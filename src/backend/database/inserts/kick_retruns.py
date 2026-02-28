from inserts.utils.bulk_insert import bulk_insert
import psycopg2
from psycopg2 import DatabaseError, IntegrityError
from utils.logging import logger

# Function that takes in a cursor, flat stat list, and the player mapping
# and inserts the kick return player stats into PostgreSQL

def insert_kick_return_player_stats(cursor, stat_list, player_map):
    kick_return_values = []
    for s in stat_list:
        internal_player_id = player_map.get(s["player_id"])

        if not internal_player_id:
            logger.warning(f"Unknown player (player_id : {s['player_id']}), skipping player.")
            continue

        kick_return_values.append((
            internal_player_id,
            s["game_id"],
            s["total_kick_returns"],
            s["kick_return_yards"],
            s["kick_return_average"],
            s["kick_return_long"],
            s["td"],
            s["kick_return_td"],
            s["exp_return_td"]
        ))

    if not kick_return_values:
        logger.warning("No kick return data present")
        return

    try:
        bulk_insert(
            cursor=cursor,
            table_name="player_kick_return_stats",
            columns=[
                "player_id",
                "game_id",
                "total_kick_returns",
                "kick_return_yards",
                "kick_return_average",
                "kick_return_long",
                "td",
                "kick_return_td",
                "exp_return_td"
            ],
            values=kick_return_values,
            conflict_columns=["player_id", "game_id"]
        )
    except IntegrityError as e:
        logger.warning(f"Duplicate entry detected or constraint violation: {e}")
    except DatabaseError as e:
        logger.error(f"Database error occurred: {e}")
        raise
