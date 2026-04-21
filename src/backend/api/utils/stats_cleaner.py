
# Remove stat group if it is in fact empty
def remove_empty_stat_groups(stats: dict) -> dict:
    cleaned = {}

    for group_name, group_values in stats.items():
        if not isinstance(group_values, dict):
            continue
        if group_values == {}:
            cleaned[group_name] = {}
            continue
        if all(v in (0, None) for v in group_values.values()):
            cleaned[group_name] = {}
        else:
            cleaned[group_name] = group_values

    return cleaned

def apply_stat_cleanup(player_data):
     for team in ["away_team", "home_team"]:
         for player in player_data.get(team, []):
             player["stats"] = remove_empty_stat_groups(player["stats"])
     return player_data
