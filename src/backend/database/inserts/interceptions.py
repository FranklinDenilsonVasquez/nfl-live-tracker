from src.backend.database.inserts.utils.bulk_insert import bulk_insert
import psycopg2
from psycopg2 import DatabaseError, IntegrityError
from src.backend.utils.logging import logger

# Function that takes in a cursor, flat stat list, and the player mapping
# and inserts the interception player stats into PostgreSQL

def insert_interception_player_stats(cursor, stat_list, player_map):
    interception_values = []
    for s in stat_list:
        internal_player_id = player_map.get(s["player_id"])

        if not internal_player_id:
            logger.warning(f"Unknown player (player_id : {s['player_id']}), skipping player.")
            continue

        interception_values.append((
            internal_player_id,
            s["game_id"],
            s["total_interceptions"],
            s["yards"],
            s["intercepted_touch_downs"]
        ))

    if not interception_values:
        logger.warning(f"No interception data present")
        return

    try:
        bulk_insert(
            cursor=cursor,
            table_name="player_interception_stats",
            columns=[
                "player_id",
                "game_id",
                "total_interceptions",
                "yards",
                "intercepted_touch_downs"
            ],
            values=interception_values,
            conflict_columns=["player_id", "game_id"]
        )
    except IntegrityError as e:
        logger.warning(f"Duplicate entry detected or constraint violation: {e}")
    except DatabaseError as e:
        logger.error(f"Database error occurred: {e}")
        raise