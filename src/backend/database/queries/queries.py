from motor.docstrings import cursor_sort_doc

from src.backend.database.db_connection import get_db_connection

def get_players_by_team (team_id: int, season: int):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            p.player_id, 
            p.player_name, 
            pos.position_name, 
            p.player_img, 
            pt.jersey_number, 
            s.season_year
        FROM player_team AS pt
        JOIN player AS p ON pt.api_player_id = p.api_player_id
        JOIN position AS pos ON p.position_id = pos.position_id
        JOIN season AS s ON pt.season_id = s.season_id
        WHERE pt.team_id = %s AND s.season_year = %s
        ORDER BY p.player_name;
    """, (team_id, str(season)))

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

def get_all_teams():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            t.team_id,
            t.team_name,
            t.city,
            t.code,
            t.logo_path,
            s.stadium_id,
            s.stadium_name,
            s.location,
            s.capacity
        FROM team AS t 
        JOIN stadium AS s ON t.stadium_id = s.stadium_id
        ORDER BY team_name;
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows
