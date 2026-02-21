from .utils import normalize_stat_list

def normalize_rushing_stats(stat_list):
    rushing_mapping = {
        "total rushes" : {
            "type" : "int",
            "column" : "total_rushes"
        },
        "yards": {
            "type": "int",
            "column": "rushing_yards"
        },
        "average": {
            "type": "float",
            "column": "rushing_average"
        },
        "rushing touch downs": {
            "type": "int",
            "column": "rushing_touchdowns"
        },
        "longest rush": {
            "type": "int",
            "column": "longest_rush"
        },
        "two pt": {
            "type": "int",
            "column": "two_point_rushes"
        },
        "kick return td": {
            "type": "int",
            "column": "kick_return_touchdowns"
        },
        "exp return td": {
            "type": "int",
            "column": "exp_return_touchdowns"
        },
    }

    normalized_rushing_stats = normalize_stat_list(stat_list, rushing_mapping)

    return normalized_rushing_stats