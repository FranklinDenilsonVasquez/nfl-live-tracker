from inserts.utils.bulk_insert import bulk_insert
import psycopg2
from psycopg2 import DatabaseError, IntegrityError
from utils.logging import logger

# Function that takes in a cursor, flat stat list, and the player mapping
# and inserts the rushing player stats into PostgreSQL
def insert_rushing_player_stats(cursor, stat_list, player_map):
    rushing_values = []
    for s in stat_list:
        internal_player_id = player_map.get(s["player_id"])

        if not internal_player_id:
            logger.warning(f"Unknown player (player_id : {s['player_id']}), skipping player.")
            continue

        rushing_values.append((
            internal_player_id,
            s["game_id"],
            s["total_rushes"],
            s["rushing_yards"],
            s["rushing_average"],
            s["rushing_touchdowns"],
            s["longest_rush"],
            s["two_point_rushes"],
            s["kick_return_touchdowns"],
            s["exp_return_touchdowns"]
        ))

    if not rushing_values:
        logger.warning("No kicking data present")
        return

    try:
        bulk_insert(
            cursor=cursor,
            table_name="player_rushing_stats",
            columns=[
                "player_id",
                "game_id",
                "total_rushes",
                "rushing_yards",
                "rushing_average",
                "rushing_touchdowns",
                "longest_rush",
                "two_point_rushes",
                "kick_return_touchdowns",
                "exp_return_touchdowns"
            ],
            values=rushing_values,
            conflict_columns=["player_id", "game_id"]
        )
    except IntegrityError as e:
        logger.warning(f"Duplicate entry detected or constraint violation: {e}")
    except DatabaseError as e:
        logger.error(f"Database error occurred: {e}")
        raise