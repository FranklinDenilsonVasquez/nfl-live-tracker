from backend.db.db_connection import get_db_connection
from backend.db.db_config import get_db_config
from backend.utils.logging import setup_logger
import mysql.connector
from datetime import datetime


logger = setup_logger()

def insert_teams(teams):
    # Establish database connection
    conn = get_db_connection()
    if conn is None:
        logger.error("Could not connect to the database.")
        return     

    cursor = conn.cursor()
    
    # Iterate over teams and insert them into the database
    for team in teams:
        
        sql = """INSERT IGNORE INTO team (teamId, teamName, city, state, logoPath)
                 VALUES (%s, %s, %s, %s, %s)"""
        team_data = (
            team['id'],
            team['name'],
            team['city'], 
            team['code'],
            team['logo']
        )
        try:
            cursor.execute(sql, team_data)
        except mysql.connector.Error as e:
            print(f"Error inserting team {team['name']}, {e}")
            continue
    conn.commit()
    cursor.close()
    conn.close()


def insert_players(players, team_id):
    # Establish database connection
    conn = get_db_connection()
    
    if conn is None:
        logger.error("Could not connect to the database.")
        return      
    cursor = conn.cursor()

    # Normalize the roster status of each player to keep track of their current status
    def get_roster_status(group):
            if not group:
                return 'active'
            group = group.lower()
            if "practice" in group:
                return "practice_squad"
            elif "injured" in group:
                return "injured_reserve"
            return "active"
    
    # Normalize position type and get it ready for the database
    def normalize_position_type(group):
        if not group:
            return None
        group = group.lower()
        if "offense" in group:
            return "offense"
        elif "defense" in group:
            return "defense"
        elif "special" in group:
            return "special_teams"
        elif "practice" in group or "injured" in group:
            return None
        else:
            logger.warning(f"Unrecognized group label '{group}' for positionType.")
            return None

    # Iterate over teams and insert payers into the database
    for player in players:
        try:
            # Check required fields
            if 'id' not in player or 'name' not in player or 'position' not in player:
                logger.warning(f"Skipping malformed player data: {player}")
                continue

            player_id = player['id']
            full_name = player['name']
            position_name = player.get('position') # May be None
            group = player.get('group')
            position_type = normalize_position_type(group)
            roster_status = get_roster_status(group)

            if position_type is None:
                logger.warning(f"Unknown positionType for player {player_id} - {full_name}, group='{player.get('group')}', inserting with NULL.")

            # Try to get positionId, if position_name is available
            position_id = None
            if position_name:
                cursor.execute("SELECT positionId FROM position WHERE positionName = %s", (position_name,))
                result = cursor.fetchone()
                if result:
                    position_id = result[0]
                else:
                    cursor.execute("INSERT INTO position (positionName) VALUES (%s)", (position_name,))
                    conn.commit()
                    position_id = cursor.lastrowid
            else:
                logger.warning(f"Player {player_id} - {full_name} has no positionName.")


            # Prepare insert (ON DUPLICATE KEY UPDATE only updates if player already exists)
            sql = """
                INSERT INTO player (playerId, teamId, positionId, positionType, fullName, rosterStatus)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    teamId = VALUES(teamId),
                    positionId = VALUES(positionId),
                    positionType = VALUES(positionType),
                    fullName = VALUES(fullName),
                    rosterStatus = VALUES(rosterStatus)
                """
            player_data = (player_id, team_id, position_id, position_type, full_name, roster_status)

            cursor.execute(sql, player_data)

        except Exception as e:
            logger.warning(f"Failed to insert player {player.get('id', 'UNKNOWN')}: {e}")
            continue


    conn.commit()
    cursor.close()
    conn.close()
    logger.info(f"Finished inserting players for team ID {team_id}.")

# Function to insert coaches into the database
def insert_coach_from_team(team):
    # Establish database connection
    conn = get_db_connection()
    
    if conn is None:
        logger.error("Could not connect to the database.")
        return      
    cursor = conn.cursor()

    try:
        team_id = team['id']
        coach_name = team.get("coach", None)

        # If no coach is listed for the team send a warning 
        if not coach_name:
            logger.warning(f"No coach info found for team {team_id} - {team['name']}")
            return 
        
        # strip() = remove leading and trailing characters
        coach_name = coach_name.strip()
        
        # Prepare the SQL statment to insert coaches into the coach table
        sql = """
            INSERT INTO coach (teamId, fullName)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE 
                fullName = VALUES(fullName)
            """
        cursor.execute(sql, (team_id, coach_name))

    except Exception as e:
        logger.warning(f"Failed to insert coach from team {team_id} - {team['name']}: {e}")

    finally:
        conn.commit()
        cursor.close()
        conn.close()
        logger.info("Finished inserting coaches into database")


def insert_seasons(season_years):
    # Establish database connection
    conn = get_db_connection()
    if conn is None:
        logger.error("Could not connect to the database.")
        return     

    cursor = conn.cursor()

    try:
        for year in season_years:
            sql = """
                INSERT INTO season (seasonYear)
                VALUES (%s)
                ON DUPLICATE KEY UPDATE seasonYear = VALUES(seasonYear)
            """

            cursor.execute(sql, (year,))
            logger.info(f"Inserted/Updated season: {year}")

    except Exception as e:
        logger.warning(f"Failed to insert/update season: {e}")
        
    finally:
        conn.commit()
        cursor.close()
        conn.close()
        logger.info("Finished inserting seasons into database")

def insert_games(games:list):
    # Establish database connection
    conn = get_db_connection()
    if conn is None:
        logger.error("Could not connect to the database.")
        return     

    cursor = conn.cursor()

    try:
        # Function that goes through the Season table in database and retruns it's primary key
        def get_season_id(cursor, year):
            cursor.execute("SELECT seasonId FROM season WHERE seasonYear = %s",(year,))
            row = cursor.fetchone()

            if row:
                return row[0]
            else:
                return None
            
        for game_obj in games:
            # Extract nested data by "zooming in" through the JSON structure.
            # The API response is a dictionary with keys like 'game', 'teams', etc.,
            # and each of those contains another dictionary with the actual values we need.
            # We access these step by step to safely get the data. 
            game_data = game_obj['game']
            league_data = game_obj['league']
            teams_data = game_obj['teams']
            scores_data = game_obj['scores']
            
            # Get data from the "zoomed in" JSON response
            game_id = game_data['id']
            home_team = teams_data['home']['id']
            away_team = teams_data['away']['id']
            game_date = game_data['date']['date'] # e.g., "2023-08-04"

            home_score = scores_data['home'].get('total', 0) # Get total if set to None return 0 to not raise an error
            away_score = scores_data['away'].get('total', 0) # Get total if set to None return 0 to not raise an error
            
            # If score is NULL pass 0
            home_score = home_score if home_score is not None else 0
            away_score = away_score if away_score is not None else 0

            status = game_data['status']['long']
            stage = game_data.get('stage')
            week = game_data.get('week')
            game_venue = game_data['venue'].get('name', 0)
            game_city = game_data['venue'].get('city', 0)
            game_season = league_data['season']

            season_id = get_season_id(cursor, game_season)

            if not season_id:
                logger.warning(f"SeasonId dosen't exist in database. Skipping game {game_id}")
                continue


            sql = """
                INSERT INTO game(gameId, homeTeamId, awayTeamId, gameDate, 
                                homeTeamScore, awayTeamScore, seasonId, status, stage, week, venue, city)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE 
                    homeTeamScore = VALUES(homeTeamScore),
                    awayTeamScore = VALUES(awayTeamScore),
                    gameDate = VALUES(gameDate),
                    seasonId = VALUES(seasonId),
                    status = VALUES(status), 
                    stage = VALUES(stage),
                    week = VALUES(week),
                    venue = VALUES(venue),
                    city = VALUES(city) 
            """

            data = (game_id, home_team, away_team,game_date, home_score, 
                    away_score, season_id, status, stage, week, game_venue, game_city)

            cursor.execute(sql, data)

    except Exception as e:
        logger.warning(f"Failed to insert game data: {e}")

    finally:
        conn.commit()
        cursor.close()
        conn.close()
        logger.info("Finished inserting games into database")


