from inserts.utils.bulk_insert import bulk_insert
import psycopg2
from psycopg2 import DatabaseError, IntegrityError
from utils.logging import logger

# Function that takes in a cursor, flat stat list, and the player mapping
# and inserts the punt return player stats into PostgreSQL
def insert_punt_return_player_stats(cursor, stat_list, player_map):
    punt_return_values = []
    for s in stat_list:
        internal_player_id = player_map.get(s["player_id"])

        if not internal_player_id:
            logger.warning(f"Unknown player (player_id : {s['player_id']}), skipping player.")
            continue

        punt_return_values.append((
            internal_player_id,
            s["game_id"],
            s["total"],
            s["yards"],
            s["average"],
            s["long"],
            s["touchdown"]
        ))

    if not punt_return_values:
        logger.warning("No kicking data present")
        return

    try:
        bulk_insert(
            cursor=cursor,
            table_name="player_punt_return_stats",
            columns=[
                "player_id",
                "game_id",
                "total",
                "yards",
                "average",
                "long",
                "touchdown"
            ],
            values=punt_return_values,
            conflict_columns=["player_id", "game_id"]
        )
    except IntegrityError as e:
        logger.warning(f"Duplicate entry detected or constraint violation: {e}")
    except DatabaseError as e:
        logger.error(f"Database error occurred: {e}")
        raise