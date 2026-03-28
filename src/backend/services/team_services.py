from src.backend.utils.logging import logger
from pprint import pprint
from src.backend.database.db_connection import get_db_connection

# Service to establish connection and calling a query that returns a certain teams details
def get_team_details(team_id: int):
    conn = get_db_connection()

    if not conn:
        raise Exception("Failed to connect to database")
    try:
        with conn.cursor() as cursor:
            from src.backend.database.queries.team_queries import get_team_info
            team_details = get_team_info(cursor, team_id)
            pprint(team_details)

            if not team_details:
                logger.warning(f"Error getting team details for team : {team_id}")
                return None

            return team_details
    finally:
        conn.close()