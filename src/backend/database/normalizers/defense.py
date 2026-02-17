from .utils import normalize_stat_list

def normalize_defense_stats(stat_list):
    defense_mapping = {
        "tackles" : "tackles",
        "unassisted tackles": "unassisted_tackles",
        "sacks" : "sacks",
        "tfl" : "tackles_for_loss",
        "passes defended" : "passes_defended",
        "qb hts" : "qb_hits",
        "interceptions for touch downs" : "interceptions_for_tds",
        "blocked kicks" : "blocked_kicks",
        "kick return td" : "kick_return_td",
        "exp return td" : "expected_return_td",
        "ff" : "forced_fumbles"
    }

    normalize = normalize_stat_list(stat_list, defense_mapping)

    return normalize
