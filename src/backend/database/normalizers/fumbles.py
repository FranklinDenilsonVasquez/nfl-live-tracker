from .utils import normalize_stat_list

def normalize_fumbles_stats(stat_list):
    fumbles_mapping = {
        "total" : "total_fumbles",
        "lost" : "fumble_lost",
        "rec" : "fumble_recovery",
        "rec td" : "fumble_recovery_td"
    }

    normalized_fumbles = normalize_stat_list(stat_list, fumbles_mapping)

    return normalized_fumbles