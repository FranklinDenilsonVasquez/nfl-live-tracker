from .utils import normalize_stat_list

def normalize_interception_stats(stat_list):
    interception_mapping= {
        "total interceptions" : "total_interceptions",
        "yards" : "yards",
        "intercepted touch downs" : "intercepted_touch_downs"
    }

    normalized_interceptions = normalize_stat_list(stat_list, interception_mapping)

    return normalized_interceptions