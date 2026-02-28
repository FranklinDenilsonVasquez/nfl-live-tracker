from inserts.utils.bulk_insert import bulk_insert
import psycopg2
from psycopg2 import DatabaseError, IntegrityError
from utils.logging import logger

# Function that takes in a cursor, flat stat list, and the player mapping
# and inserts the punting player stats into PostgreSQL
def insert_punting_player_stats(cursor, stat_list, player_map):
    punting_values = []
    for s in stat_list:
        internal_player_id = player_map.get(s["player_id"])

        if not internal_player_id:
            logger.warning(f"Unknown player (player_id : {s['player_id']}), skipping player.")
            continue

        punting_values.append((
            internal_player_id,
            s["game_id"],
            s["punt_total"],
            s["punt_yards"],
            s["punt_average"],
            s["touchbacks"],
            s["inside_20"],
            s["long_punt"]
        ))
    if not punting_values:
        logger.warning("No kicking data present")
        return

    try:
        bulk_insert(
            cursor=cursor,
            table_name="player_punting_stats",
            columns=[
                "player_id",
                "game_id",
                "punt_total",
                "punt_yards",
                "punt_average",
                "touchbacks",
                "inside_20",
                "long_punt"
            ],
            values=punting_values,
            conflict_columns=["player_id", "game_id"]
        )
    except IntegrityError as e:
        logger.warning(f"Duplicate entry detected or constraint violation: {e}")
    except DatabaseError as e:
        logger.error(f"Database error occurred: {e}")
        raise