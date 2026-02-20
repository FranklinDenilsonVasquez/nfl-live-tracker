from .utils import normalize_stat_list

def normalize_defense_stats(stat_list):
    defense_mapping = {
        "tackles" : {
            "type" : "int",
            "column" : "tackles"
        },
        "unassisted tackles": {
            "type" : "int",
            "column" : "unassisted_tackles"
        },
        "sacks" : {
            "type" : "int",
            "column" : "sacks"
        },
        "tfl" : {
            "type" : "int",
            "column" : "tackles_for_loss"
        },
        "passes defended" : {
            "type" : "int",
            "column" : "passes_defended"
        },
        "qb hts" : {
            "type" : "int",
            "column" : "qb_hits"
        },
        "interceptions for touch downs" : {
            "type" : "int",
            "column" : "interceptions_for_tds"
        },
        "blocked kicks" : {
            "type" : "int",
            "column" : "blocked_kicks"
        },
        "kick return td" : {
            "type" : "int",
            "column" : "kick_return_td"
        },
        "exp return td" : {
            "type" : "int",
            "column" : "expected_return_td"
        },
        "ff" : {
            "type" : "int",
            "column" : "forced_fumbles"
        }
    }

    normalized_defense = normalize_stat_list(stat_list, defense_mapping)

    return normalized_defense
