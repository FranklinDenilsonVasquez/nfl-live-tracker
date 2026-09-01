# Function that takes in a flat stat list, grabs each player in that stat list
# and then looks up its db player_id
def get_player_map_for_stats(cursor, stat_list):
    if not stat_list:
        return {}

    # Debugging
    for i, s in enumerate(stat_list):
        if not isinstance(s, dict):
            print(f"Element {i} in stat_list if not a dict: {s}")
    api_player_ids = list({
        s["player_id"]
        for s in stat_list
    })

    if not api_player_ids:
        return {}

    cursor.execute("""
        SELECT api_player_id, player_id 
        FROM player
        WHERE api_player_id = ANY(%s);
    """,
        (api_player_ids,)
    )

    rows = cursor.fetchall()
    return {row[0]: row[1] for row in rows}

# Function that takes internal player_id values and returns each player's
# position name, for use by the rating calculation (which is position-specific)
def get_player_position_map(cursor, internal_player_ids):
    if not internal_player_ids:
        return {}

    cursor.execute("""
        SELECT p.player_id, ps.position_name
        FROM player AS p
        INNER JOIN position AS ps ON p.position_id = ps.position_id
        WHERE p.player_id = ANY(%s);
    """,
        (list(internal_player_ids),)
    )

    rows = cursor.fetchall()
    return {row[0]: row[1] for row in rows}