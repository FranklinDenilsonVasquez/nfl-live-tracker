from inserts.utils.bulk_insert import bulk_insert
import psycopg2
from psycopg2 import DatabaseError, IntegrityError
from utils.logging import logger

# Function that takes in a cursor, flat stat list, and the player mapping
# and inserts the passing player stats into PostgreSQL
def insert_player_passing_stats(cursor, stat_list, player_map):
    passing_values = []
    for s in stat_list:
        internal_player_id = player_map.get(s["player_id"])

        if not internal_player_id:
            logger.warning(f"Unknown player (player_id : {s['player_id']}), skipping player.")
            continue

        passing_values.append((
            internal_player_id,
            s["game_id"],
            s["passing_completion"],
            s["passing_attempted"],
            s["passing_yards"],
            s["passing_average"],
            s["passing_touch_downs"],
            s["passing_interceptions"],
            s["sacks_total"],
            s["sack_yards"],
            s["passer_rating"],
            s["two_point_conversions"]
        ))

    if not passing_values:
        logger.warning("No kicking data present")
        return

    try:
        bulk_insert(
            cursor=cursor,
            table_name="player_passing_stats",
            columns=[
                "player_id",
                "game_id",
                "passing_completion",
                "passing_attempted",
                "passing_yards",
                "passing_average",
                "passing_touch_downs",
                "passing_interceptions",
                "sacks_total",
                "sack_yards",
                "passer_rating",
                "two_point_conversions"
            ],
            values=passing_values,
            conflict_columns=["player_id", "game_id"]
        )
    except IntegrityError as e:
        logger.warning(f"Duplicate entry detected or constraint violation: {e}")
    except DatabaseError as e:
        logger.error(f"Database error occurred: {e}")
        raise