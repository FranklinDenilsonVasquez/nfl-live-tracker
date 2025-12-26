from src.backend.api.fetch_data import fetch_teams, fetch_players, fetch_season, fetch_game_for_season, fetch_player_stats
from src.backend.db.insert_data import insert_teams, insert_players, insert_coach_from_team, insert_seasons, insert_games, process_and_insert_stats
from src.backend.utils.logging import setup_logger
from pprint import pprint   
import pprint                        # Formats the data cleaner
import time
from src.backend.db.db_config import get_db_config


logger = setup_logger() 


def main():
    # Fetch data
    teams           = fetch_teams()
    seasons          = fetch_season()
    logger.info(f"Fetched {len(teams)} teams.")


    #for season in seasons:
    try:
        insert_seasons(seasons)
    except Exception as e:
        logger.warning(f"Something went wrong {e}")


    # Insert players and coach team by team
    # for season_year in range(2021, 2022): # range(2021,2024) to run from 2021-2023 because of the free plan (API)
    #     logger.info(f"Processing season : {season_year}")
    #     for team in teams:
    #         team_id = team['id']
    #         team_name = team['name']
    #         try:
    #             players = fetch_players(team_id, season_year)
    #             player_length = len(players)
    #             logger.info(f"Fetched {len(players)} players for {team_name} (ID {team_id})")
    #             if player_length == 0:
    #                 logger.warning(f"Zero players for team: {team_name} (ID {team_id})")
    #
    #             # insert_players(players, team_id, season_year)
    #             #insert_coach_from_team(team)
    #             time.sleep(7)
    #         except Exception as e:
    #             logger.warning(f"Failed to fetch players for {team_name} (ID {team_id}): {e}")
    #
        # logger.info(f"Fetching games for the season {season_year}.")

        # Insert Games and Stats for each game.
        # games = fetch_game_for_season(season_year)
        # logger.info(f"Fetched {len(games)} games for season {season_year}.")
        # insert_games(games)
        # for game in games:
        #     try:
        #         process_and_insert_stats(game, season_year)
        #     except Exception as e:
        #         logger.warning(f"Failed to insert player stats for game {game} in season {season_year}: {e}")
        # time.sleep(1)

    # Conditionally run this if the season table is not populated.
    #insert_seasons(seasons)
    

    
if __name__ == "__main__":
    main()