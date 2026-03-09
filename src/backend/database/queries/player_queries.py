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

