from src.backend.utils.logging import logger
from psycopg2.extras import RealDictCursor
from pprint import pprint

def get_standings(cursor, season_id: int):
    try:
        query = """
            SELECT 
                t.team_id,
                t.team_name,
                t.logo_path, 
                s.conference, 
                s.division, 
                s.position,
                s.wins,
                s.losses,
                s.ties,
                s.points_for,
                s.points_against,
                s.point_differential,
                s.conference_wins,
                s.conference_losses,
                s.division_wins,
                s.division_losses,
                s.home_wins,
                s.home_losses,
                s.road_wins,
                s.road_losses,
                s.streak
            FROM standings s 
            JOIN team t ON (s.team_id = t.team_id)
            WHERE s.season_id = %s
            ORDER BY conference, 
                CASE division
                    WHEN 'North' THEN 1
                    WHEN 'East' THEN 2
                    WHEN 'South' THEN 3
                    WHEN 'West' THEN 4
                    ELSE 99
                END, 
            position;
        """

        with cursor.connection.cursor(cursor_factory=RealDictCursor) as new_cursor:
            new_cursor.execute(query, (season_id, ))
            data = new_cursor.fetchall()

        if not data:
            logger.warning(f"No data found for standings in season : {season_id}")
            return None

        # pprint(data)
        return data

    except Exception as e:
        logger.warning(f"Error when executing 'get_standings()' : {e}")
        return None