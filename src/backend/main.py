from backend.api.fetch_data import fetch_teams, fetch_players, feth_season, fetch_game_for_season
from backend.db.insert_data import insert_teams, insert_players, insert_coach_from_team, insert_seasons, insert_games
from backend.utils.logging import setup_logger
from pprint import pprint   
import pprint                        # Formats the data cleaner
import time
from backend.db.db_config import get_db_config


logger = setup_logger() 


def main():
    # Fetch data
    teams           = fetch_teams()
    seasons          = feth_season()
    logger.info(f"Fetched {len(teams)} teams.")

    # Insert players and coach team by team 
    for team in teams:
        team_id = team['id']
        team_name = team['name']
        try:
            players = fetch_players(team_id)
            logger.info(f"Fetched{len(players)} players for {team_name} (ID {team_id})")
            insert_players(players, team_id)
            insert_coach_from_team(team)
            time.sleep(1)
        except Exception as e:
            logger.warning(f"Failed to fetch players for {team_name} (ID {team_id}): {e}")
    
    # Conditionally run this if the season table is not populated.
    #insert_seasons(seasons)
    for season in seasons:
        logger.info(f"Fetching games for the season {season}.")
        games = fetch_game_for_season(season)
        logger.info(f"Fetched {len(games)} games for season {season}.")
        insert_games(games)
        time.sleep(1)
    

    
if __name__ == "__main__":
    main()