from src.backend.api.fetch_data import fetch_teams, fetch_season, fetch_game_for_season, fetch_player_stats
from src.backend.database.inserts.insert_data import (process_and_insert_stats)
from src.backend.utils.logging import setup_logger
import time
from pprint import pprint

logger = setup_logger()


def main():
    # Fetch data
    #teams = fetch_teams()
    seasons = fetch_season()
    game_id = 4000
    player_stats = fetch_player_stats(game_id)
    if player_stats:
        print(f"Fetched player stats for game_id = {game_id}")
        pprint(player_stats)
    #logger.info(f"Fetched {len(teams)} teams.")

    # Insert seasons and teams into DB
    # try:
    #     insert_seasons(seasons)
    #     insert_teams(teams)
    #     insert_stadium(teams)
    # except Exception as e:
    #     logger.warning(f"Something went wrong {e}")

    # Insert players and coach team by team
    # for season_year in range(2022, 2025):  # range(2022,2025) to run from 2022-2024 because of the free plan (API)
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
        #             insert_players(players, team_id, season_year)
        #             #insert_coach_from_team(team, season_year)
        #             #logger.info(f"Finished adding coaches into database")
        #             time.sleep(7)
        #         except Exception as e:
        #             logger.warning(f"Failed to fetch players for {team_name} (ID {team_id}): {e}")
        #             #logger.warning(f"Failed to insert coach for {team_name} (ID {team_id}): {e}")

        # logger.info(f"Fetching games for the season {season_year}.")

        # Insert Games and Stats for each game.
        # games = fetch_game_for_season(season_year)
        #logger.info(f"Fetched {len(games)} games for season {season_year}.")
        # insert_games(games)
        # for game in games:
        #     api_game_id = None
        #     try:
        #         api_game_id = game.get("game", {}).get("id")
        #
        #         if not api_game_id:
        #             logger.warning(f"Skipping game with missing API id: {game}")
        #             continue
        #
        #         process_and_insert_stats(api_game_id, season_year)
        #         time.sleep(10)
        #     except Exception as e:
        #         logger.warning(f"Failed to insert player stats for game_id = {api_game_id} in season {season_year}: {e}")
        # time.sleep(5)

    # Conditionally run this if the season table is not populated.
    # insert_seasons(seasons)


if __name__ == "__main__":
    main()