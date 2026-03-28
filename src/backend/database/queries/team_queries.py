from src.backend.utils.logging import logger
from psycopg2.extras import RealDictCursor

# Query to get team info given a team_id
def get_team_info(cursor, team_id: int):
    try:
        query = """
            SELECT 
                t.team_id AS "team_id",
                t.team_name AS "team_name",
                t.city AS "city",
                t.code AS "code",
                t.logo_path AS "logo",
                json_build_object(
                    'stadium_id', s.stadium_id,
                    'name', s.stadium_name,
                    'capacity', s.capacity,
                    'location', s.location
                ) AS stadium
            FROM team t 
            JOIN stadium s ON t.stadium_id = s.stadium_id
            WHERE t.team_id = %s
        """

        with cursor.connection.cursor(cursor_factory=RealDictCursor) as new_cursor:
            new_cursor.execute(query, (team_id,))
            data = new_cursor.fetchone()

            if not data:
                logger.warning(f"No data found for team : {team_id}")
                return None

            return data

    except Exception as e:
        logger.warning(f"Error when executing 'get_team_info()' : {e}")
        return None