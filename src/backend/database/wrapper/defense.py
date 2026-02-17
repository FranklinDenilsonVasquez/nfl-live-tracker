from database.normalizers.defense import normalize_defense_stats

# Wrapper: Loops over team -> players -> calls normalize_player_defense
def normalize_game_response(game_response, group_name, normalize_func, game_id=None):
    # Normalize the defensive stats from the full API response for a game
    normalized_players = []

    for team_data in game_response:
        team_id = team_data.get("team", {}).get("id")
        groups = team_data.get("groups", [])

        for group in groups:
            # Defensive stat group
            if group.get("name", "").lower() == group_name.lower():
                for player_data in group.get("players", []):
                    player_id = player_data.get("player",{}).get("id")
                    stats_list = player_data.get("statistics", [])

                    normalized_stats = normalize_func(stats_list)

                    # Include game_id, player_id, and team_id for DB insertion
                    normalized_stats["player_id"] = player_id
                    normalized_stats["team_id"] = team_id
                    if game_id is not None:
                        normalized_stats["game_id"] = game_id

                    normalized_players.append(normalized_stats)

    return normalized_players
