from api.fetch_data import fetch_player_stats as api_player_stats
from database.services.player_game_stats_service import orchestrate_player_game_stats
from pprint import pprint

def ingest_player_game_stats(game_id:int):
    game_response = api_player_stats(game_id)

    if not game_response:
        print(f"No data found for player in game_id = {game_id}")
        return

    all_stats = orchestrate_player_game_stats(game_response, game_id)

    print(f"Processing {len(all_stats)} player stat rows")
    pprint(all_stats)

if __name__ == "__main__":
    ingest_player_game_stats(4000)
