from psycopg2 import DatabaseError, IntegrityError
from .utils.bulk_insert import bulk_insert
from src.backend.utils.logging import logger

def insert_standings(cursor, standing_list):
    values = []

    for s in standing_list:
        values.append((
            s["season_id"],
            s["team_id"],
            s["conference"],
            s["division"],
            s["position"],
            s["wins"],
            s["losses"],
            s["ties"],
            s["points_for"],
            s["points_against"],
            s["point_differential"],
            s["conference_wins"],
            s["conference_losses"],
            s["division_wins"],
            s["division_losses"],
            s["home_wins"],
            s["home_losses"],
            s["road_wins"],
            s["road_losses"],
            s["streak"]
        ))

    try:
        bulk_insert(
            cursor=cursor,
            table_name="standings",
            columns=[
                "season_id",
                "team_id",
                "conference",
                "division",
                "position",
                "wins",
                "losses",
                "ties",
                "points_for",
                "points_against",
                "point_differential",
                "conference_wins",
                "conference_losses",
                "division_wins",
                "division_losses",
                "home_wins",
                "home_losses",
                "road_wins",
                "road_losses",
                "streak"
            ],
            values=values,
            conflict_columns=[
                "season_id",
                "team_id"
            ]
        )
    except IntegrityError as e:
        logger.warning(f"Duplicate entry detected or constraint violation: {e}")
    except DatabaseError as e:
        logger.error(f"Database error occurred: {e}")
        raise
        