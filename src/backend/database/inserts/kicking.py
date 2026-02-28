from src.backend.database.inserts.utils.bulk_insert import bulk_insert
import psycopg2
from psycopg2 import DatabaseError, IntegrityError
from src.backend.utils.logging import logger

# Function that takes in a cursor, flat stat list, and the player mapping
# and inserts the kicking player stats into PostgreSQL

def insert_kicking_player_stats(cursor, stat_list, player_map):
    kicking_values = []
    for s in stat_list:
        internal_player_id = player_map.get(s["player_id"])

        if not internal_player_id:
            logger.warning(f"Unknown player (player_id : {s['player_id']}), skipping player.")
            continue

        kicking_values.append((
            internal_player_id,
            s["game_id"],
            s["fg_made"],
            s["fg_attempted"],
            s["fg_percentage"],
            s["long"],
            s["xp_made"],
            s["xp_attempted"],
            s["points"],
            s["field_goals_from_1_19_yards"],
            s["field_goals_from_20_29_yards"],
            s["field_goals_from_30_39_yards"],
            s["field_goals_from_40_49_yards"],
            s["field_goals_from_50_yards"]
        ))

    if not kicking_values:
        logger.warning("No kicking data present")
        return

    try:
        bulk_insert(
            cursor=cursor,
            table_name="player_kicking_stats",
            columns=[
                "player_id",
                "game_id",
                "fg_made",
                "fg_attempted",
                "fg_percentage",
                "long",
                "xp_made",
                "xp_attempted",
                "points",
                "field_goals_from_1_19_yards",
                "field_goals_from_20_29_yards",
                "field_goals_from_30_39_yards",
                "field_goals_from_40_49_yards",
                "field_goals_from_50_yards"
            ],
            values=kicking_values,
            conflict_columns=["player_id", "game_id"]
        )
    except IntegrityError as e:
        logger.warning(f"Duplicate entry detected or constraint violation: {e}")
    except DatabaseError as e:
        logger.error(f"Database error occurred: {e}")
        raise