
def player_exists(cursor, player_id):
    query = """
        SELECT player
        FROM player
        WHERE api_player_id = %s  
        LIMIT 1 
    """

    cursor.execute(query, (player_id,))
    return cursor.fetchone() is not None