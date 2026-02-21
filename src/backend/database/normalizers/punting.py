from .utils import normalize_stat_list

def normalize_punting_stats(stat_list):
    punting_mapping = {
        "total" : {
            "type" : "int",
            "column" : "punt_total"
        },
        "yards" : {
            "type" : "int",
            "column" : "punt_yards"
        },
        "average" : {
            "type" : "float",
            "column" : "punt_average"
        },
        "touchbacks" : {
            "type" : "int",
            "column" : "touchbacks"
        },
        "in20" : {
            "type" : "int",
            "column" : "inside_20"
        },
        "lg" : {
            "type" : "int",
            "column" : "long_punt"
        }
    }

    normalized_punting_stats = normalize_stat_list(stat_list, punting_mapping)

    return normalized_punting_stats