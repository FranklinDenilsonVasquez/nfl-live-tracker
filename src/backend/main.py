from backend.api.fetch_data import fetch_teams, fetch_players
from backend.db.insert_data import insert_teams, insert_players
from backend.utils.logging import setup_logger
from pprint import pprint   
import pprint                        # Formats the data cleaner
import time
from backend.db.db_config import get_db_config


logger = setup_logger() 


def main():
    # Fetch data
    teams           = fetch_teams()
    logger.info(f"Fetched {len(teams)} teams.")

    # Insert players team by team 
    for team in teams:
        team_id = team['id']
        team_name = team['name']
        try:
            players = fetch_players(team_id)
            logger.info(f"Fetched{len(players)} players for {team_name} (ID {team_id})")
            insert_players(players, team_id)
            time.sleep(1)
        except Exception as e:
            logger.warning(f"Failed to fetch players for {team_name} (ID {team_id}): {e}")
    
    
    

    
if __name__ == "__main__":
    main()