from .utils import normalize_stat_list

def normalize_punt_return_stats(stat_list):
    punt_return_mapping = {
        "total" : {
            "type" : "int",
            "column" : "total"
        },
        "yards" : {
            "type" : "int",
            "column" : "yards"
        },
        "average" : {
            "type" : "float",
            "column" : "average"
        },
        "lg" : {
            "type" : "int",
            "column" : "long"
        },
        "td" : {
            "type" : "int",
            "column" : "touchdown"
        }
    }

    normalize_punt_return = normalize_stat_list(stat_list, punt_return_mapping)

    return normalize_punt_return