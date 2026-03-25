from src.backend.utils.logging import logger
from psycopg2.extras import RealDictCursor
# All player queries

# Get player by id
def get_player_by_id(cursor, player_id: int, season: int):
    cursor.execute("""
        SELECT p.player_name AS "player_name", 
               ps.position_name AS "position",
               p.player_img AS "img",
               pt.jersey_number AS "jersey_number", 
               p.height AS "height", 
               p.weight AS "weight", 
               p.college as "college",  
               t.team_name AS "team"
        FROM player AS p 
            INNER JOIN player_team AS pt ON p.api_player_id = pt.api_player_id
            INNER JOIN position AS ps ON p.position_id = ps.position_id
            INNER JOIN team AS t ON pt.team_id = t.team_id
            INNER JOIN season AS s ON pt.season_id = s.season_id
        WHERE p.player_id = %s AND s.season_year = %s
        ORDER BY p.player_name;
    """, (player_id, str(season))
    )
    return cursor.fetchone()

# Get player by name search
def get_player_by_name(cursor, name: str, season: int, team_id: int | None):
    base_query = """
            SELECT p.player_name AS "player_name", 
               ps.position_name AS "position",
               p.player_img AS "img",
               pt.jersey_number AS "jersey_number", 
               p.height AS "height", 
               p.weight AS "weight", 
               p.college as "college",  
               t.team_name AS "team",
                p.player_id AS "player_id"
            FROM player AS p 
                INNER JOIN player_team AS pt ON p.api_player_id = pt.api_player_id
                INNER JOIN position AS ps ON p.position_id = ps.position_id
                INNER JOIN team AS t ON pt.team_id = t.team_id
                INNER JOIN season AS s ON pt.season_id = s.season_id
            WHERE s.season_year = %s AND p.player_name ILIKE %s
        """

    params = [str(season), f"%{name}%"]
    # (f"%{name}%") : allows for partial matching

    if team_id is not None:
        base_query += " AND t.team_id = %s"
        params.append(str(team_id))

    base_query += " ORDER BY p.player_name;"

    cursor.execute(base_query, params)
    return cursor.fetchall()

# Get player stats (filter by season if given season parameter)
def get_player_stats(cursor, player_id: int, season: int | None):
    # Query that uses the predefined function to display a
    # players seasons data (Derrick Carr, 2024)
    try:
        query_function = """
               SELECT * FROM get_player_season_stats(%s, %s) AS stats
            """

        params = [player_id, season]
        # Return DB column names along with the data as a dict
        cursor = cursor.connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query_function, params)

        # Unwrap the data
        row = cursor.fetchone()
        data = row['stats']
        return data

    except Exception as e:
        logger.warning(f"Error when executing get_player_season_stats(): {e}")
        return None


def get_all_player_games_stats(cursor, player_id: int, season_id: int,
                               team_id: int | None):
    try:
        base_query = """
                SELECT * FROM get_all_player_game_stats(%s, %s) AS stats
            """

        params = [player_id, season_id]

        if team_id:
            base_query += " WHERE team_id = %s"
            params.append(team_id)

        cursor = cursor.connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute(base_query, params)
        data = cursor.fetchone()
        stats = data['stats']

        return stats

    except Exception as e:
        logger.warning(f"Error when executing get_all_player_games_stats(): {e}")
        return None