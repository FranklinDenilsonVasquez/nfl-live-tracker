from .utils import normalize_stat_list

def normalize_kick_return_stats(stat_list):
    kick_return_mapping = {
        "total" : {
            "type": "int",
            "column": "total_kick_returns"
        },
        "yards" : {
            "type" : "int",
            "column" : "kick_return_yards"
        },
        "average" : {
            "type" : "float",
            "column" : "kick_return_average"
        },
        "lg" : {
            "type" : "int",
            "column" : "kick_return_long"
        },
        "td" : {
            "type" : "int",
            "column" : "td"
        },
        "kick return td" : {
            "type" : "int",
            "column" : "kick_return_td"},
        "exp return td" : {
            "type" : "int",
            "column" : "exp_return_td"}
    }

    normalized_kick_returns = normalize_stat_list(stat_list, kick_return_mapping)

    return normalized_kick_returns