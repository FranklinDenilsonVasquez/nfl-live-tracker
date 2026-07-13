
def player_exists(cursor, player_id, season_id, team_id):
    query = """
        SELECT 1
        FROM player_team
        WHERE api_player_id = %s  AND season_id = %s AND team_id = %s
        LIMIT 1 
    """

    params = [player_id, season_id, team_id]
    cursor.execute(query, params)
    return cursor.fetchone() is not None