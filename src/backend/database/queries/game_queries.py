from src.backend.utils.logging import logger
from psycopg2.extras import RealDictCursor

# Get game list based on week and season
def get_game_list(cursor, week: str, season: int, stage: str):
    query = """
        SELECT 
            g.game_id,
            json_build_object(
                'team_id', home.team_id,
                'team_name', home.team_name,
                'stadium', json_build_object(
                    'stadium_id', st_home.stadium_id,
                    'name', st_home.stadium_name,
                    'capacity', st_home.capacity,
                    'location', st_home.location
                ),
                'city', home.city,
                'code', home.code,
                'logo', home.logo_path
            ) AS home_team,
            json_build_object(
                'team_id', away.team_id,
                'team_name', away.team_name,
                'stadium', json_build_object(
                    'stadium_id', st_away.stadium_id,
                    'name', st_away.stadium_name,
                    'capacity', st_away.capacity,
                    'location', st_away.location
                ),
                'city', away.city,
                'code', away.code,
                'logo', away.logo_path
            ) AS away_team,
            g.game_date AS date,
            g.home_team_score,
            g.away_team_score,
            json_build_object(
                'season_id', g.season_id,
                'season_year', s.season_year
            ) AS Season,
            g.status,
            g.stage,
            g.week,
            g.venue,
            g.city
        FROM game g 
        JOIN team home ON g.home_team_id = home.team_id
        JOIN team away ON g.away_team_id = away.team_id
        JOIN season s ON g.season_id = s.season_id
        JOIN stadium st_home ON home.stadium_id = st_home.stadium_id
        JOIN stadium st_away ON away.stadium_id = st_away.stadium_id
        WHERE s.season_year = %s AND g.week = %s AND g.stage = %s
        ORDER BY g.game_date;
    """

    params = [str(season), week, stage]

    cursor = cursor.connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute(query, params)
    return cursor.fetchall()

