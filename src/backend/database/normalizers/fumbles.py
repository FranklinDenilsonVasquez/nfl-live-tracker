from .utils import normalize_stat_list

def normalize_fumbles_stats(stat_list):
    fumbles_mapping = {
        "total" : {
            "type" : "int",
            "column" : "total_fumbles"
        },
        "lost" : {
            "type" : "int",
            "column" : "fumble_lost"
        },
        "rec" : {
            "type" : "int",
            "column" : "fumble_recovery"
        },
        "rec td" : {
            "type" : "int",
            "column" : "fumble_recovery_td"
        }
    }

    normalized_fumbles = normalize_stat_list(stat_list, fumbles_mapping)

    return normalized_fumbles