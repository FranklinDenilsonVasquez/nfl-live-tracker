
def get_season_id(cursor, season_year):
    query = """
        SELECT season_id 
        FROM season 
        WHERE season_year = %s
    """

    cursor.execute(query, (str(season_year), ))
    result = cursor.fetchone()

    return result[0] if result else None