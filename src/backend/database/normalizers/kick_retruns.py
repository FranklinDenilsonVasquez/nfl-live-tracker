from .utils import normalize_stat_list

def normalize_kick_return_stats(stat_list):
    kick_return_mapping = {
        "total" : "total_kick_returns",
        "yards" : "kick_return_yards",
        "average" : "kick_return_average",
        "lg" : "kick_return_long",
        "td" : "td",
        "kick return td" : "kick_return_td",
        "exp return td" : "exp_return_td"
    }

    normalized_kick_returns = normalize_stat_list(stat_list, kick_return_mapping)

    return normalized_kick_returns