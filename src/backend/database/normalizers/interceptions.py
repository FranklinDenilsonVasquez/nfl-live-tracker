from .utils import normalize_stat_list

def normalize_interception_stats(stat_list):
    interception_mapping= {
        "total interceptions" : {
            "type" : "int",
            "column" : "total_interceptions"
        },
        "yards" : {
            "type" : "int",
            "column" : "yards"
        },
        "intercepted touch downs" : {
            "type" : "int",
            "column": "intercepted_touch_downs"
        }
    }

    normalized_interceptions = normalize_stat_list(stat_list, interception_mapping)

    return normalized_interceptions