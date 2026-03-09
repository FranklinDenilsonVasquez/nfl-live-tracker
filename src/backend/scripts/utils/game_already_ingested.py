# Function that takes in cursor and game id and checks if data already in database
def game_already_exists(cursor, game_id):
    query = """
        SELECT 1 
        FROM player_passing_stats
        WHERE game_id = %s 
        LIMIT 1
    """

    cursor.execute(query, (game_id,))
    return cursor.fetchone() is not None