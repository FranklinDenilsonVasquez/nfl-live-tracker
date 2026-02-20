def normalize_stat_list(stat_list, mapping):
    normalized = {}

    # Think of this for loop as iterating inside the specific statistic
    # and the wrapper will iterate through the other data like team_id, game_id
    for stat in stat_list:
        name = stat.get("name", "").lower().strip()
        value = stat.get("value", "")

        db_key = mapping.get(name)

        if not db_key:
            continue

        stat_type = db_key["type"]

        if value in ("", "-", None):
            if stat_type == "ratio":
                col1, col2 = db_key["columns"]
                normalized[col1] = 0
                normalized[col2] = 0
            else:
                normalized[db_key["column"]] = 0
            continue
        try:
            if stat_type == "int":
                normalized[db_key["column"]] = int(value)
            elif stat_type == "float":
                normalized[db_key["column"]] = float(value)
            elif stat_type == "ratio":
                if "/" in value:
                    delimiter = "/"
                elif "-" in value:
                    delimiter = "-"
                else:
                    delimiter = None

                col1, col2 = db_key["columns"]
                if delimiter:
                    made, attempted = value.split(delimiter)
                    normalized[col1] = int(made)
                    normalized[col2] = int(attempted)
                else:
                    normalized[col1] = int(value)
                    normalized[col2] = 0
        except (ValueError, IndexError):
            if stat_type == "ratio":
                col1, col2 = db_key["columns"]
                normalized[col1] = 0
                normalized[col2] = 0
            else:
                normalized[db_key["column"]] = 0

    return normalized