def normalize_stat_list(stat_list, mapping):
    normalized = {}

    # Think of this for loop as iterating inside the specific statistic
    # and the wrapper will iterate through the other data like team_id, game_id
    for stat in stat_list:
        name = stat.get("name", "").lower().strip()
        value = stat.get("value", 0)

        db_key = mapping.get(name)

        if db_key:
            # Handel empty string or dashes
            if value in ("", "-", None):
                normalized[db_key] = 0
            else:
                try:
                    normalized[db_key] = int(value)
                except ValueError:
                    # If conversion fails default to 0
                    normalized[db_key] = 0

    return normalized