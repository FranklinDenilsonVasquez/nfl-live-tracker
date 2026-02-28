from inserts.utils.bulk_insert import bulk_insert
import psycopg2
from psycopg2 import DatabaseError, IntegrityError
from utils.logging import logger

# Function that takes in a cursor, flat stat list, and the player mapping
# and inserts the fumble player stats into PostgreSQL
def insert_fumble_player_stats(cursor, stat_list, player_map):
    fumble_values = []
    for s in stat_list:
        internal_player_id = player_map.get(s["player_id"])

        if not internal_player_id:
            logger.warning(f"Unknown player (player_id : {s['player_id']}), skipping player.")
            continue

        fumble_values.append((
            internal_player_id,
            s["game_id"],
            s["total_fumbles"],
            s["fumble_lost"],
            s["fumble_recovery"],
            s["fumble_recovery_td"]
        ))

    if not fumble_values:
        return

    try:
        bulk_insert(
            cursor=cursor,
            table_name="player_fumble_stats",
            columns=[
                "player_id",
                "game_id",
                "total_fumbles",
                "fumble_lost",
                "fumble_recovery",
                "fumble_recovery_td"
            ],
            values=fumble_values,
            conflict_columns=["player_id", "game_id"]
        )
    except IntegrityError as e:
        logger.warning(f"Duplicate entry detected or constraint violation: {e}")
    except DatabaseError as e:
        logger.error(f"Database error occurred: {e}")
        raise

