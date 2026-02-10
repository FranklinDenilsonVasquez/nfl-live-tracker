def normalize_defense_stats(stat_list):
    mapping = {
        "tackles" : "tackles",
        "unassisted tackles": "unassisted_tackles",
        "sacks" : "sacks",
        "tfl" : "tackles_for_loss",
        "passes defended" : "passes_defended",
        "qb hits" : "qb_hits",
        "interceptions for touch downs" : "interceptions_for_tds",
        "blocked kicks" : "blocked_kicks",
        "kick return td" : "kick_return_td",
        "exp return td" : "expected_return_td",
        "ff" : "forced_fumbles"
    }

    normalized = {}

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