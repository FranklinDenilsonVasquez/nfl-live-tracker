from .utils import normalize_stat_list

def normalize_passing_stats(stat_list):
    passing_mapping = {
        "comp att" : {
            "type" : "ratio",
            "columns" : ("passing_completion", "passing_attempted")
        },
        "yards" : {
            "type" : "int",
            "column" : "passing_yards"
        },
        "average" : {
            "type" : "float",
            "column" : "passing_average"
        },
        "passing touch downs" : {
            "type" : "int",
            "column" : "passing_touch_downs"
        },
        "interceptions" : {
            "type" : "int",
            "column" : "passing_interceptions"
        },
        "sacks" : {
            "type" : "ratio",
            "columns" : ("sacks_total", "sacks_yards")
        },
        "rating" : {
            "type" : "float",
            "column" : "passer_rating"
        },
        "two pt" : {
            "type" : "int",
            "column" : "two_point_conversions"
        }
    }

    passing_normalized = normalize_stat_list(stat_list, passing_mapping)

    return passing_normalized