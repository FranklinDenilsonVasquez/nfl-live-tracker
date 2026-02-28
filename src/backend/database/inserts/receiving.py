from src.backend.database.inserts.utils.bulk_insert import bulk_insert
import psycopg2
from psycopg2 import DatabaseError, IntegrityError
from src.backend.utils.logging import logger

# Function that takes in a cursor, flat stat list, and the player mapping
# and inserts the receiving player stats into PostgreSQL
def insert_receiving_player_stats(cursor, stat_list, player_map):
    receiving_values = []
    for s in stat_list:
        internal_player_id = player_map.get(s["player_id"])

        if not internal_player_id:
            logger.warning(f"Unknown player (player_id : {s['player_id']}), skipping player.")
            continue

        receiving_values.append((
            internal_player_id,
            s["game_id"],
            s["receiving_targets"],
            s["total_receptions"],
            s["receiving_yards"],
            s["receiving_average"],
            s["receiving_touchdowns"],
            s["longest_reception"],
            s["two_point_receptions"]
        ))

    if not receiving_values:
        logger.warning("No kicking data present")
        return

    try:
        bulk_insert(
            cursor=cursor,
            table_name="player_receiving_stats",
            columns=[
                "player_id",
                "game_id",
                "receiving_targets",
                "total_receptions",
                "receiving_yards",
                "receiving_average",
                "receiving_touchdowns",
                "longest_reception",
                "two_point_receptions"
            ],
            values=receiving_values,
            conflict_columns=["player_id", "game_id"]
        )
    except IntegrityError as e:
        logger.warning(f"Duplicate entry detected or constraint violation: {e}")
    except DatabaseError as e:
        logger.error(f"Database error occurred: {e}")
        raise