from .utils import normalize_stat_list

def normalize_receiving_stats(stat_list):
    receiving_mapping = {
        "targets" : {
            "type" : "int",
            "column" : "receiving_targets"
        },
        "total receptions": {
            "type": "int",
            "column": "total_receptions"
        },
        "yards": {
            "type": "int",
            "column": "receiving_yards"
        },
        "average": {
            "type": "float",
            "column": "receiving_average"
        },
        "receiving touch downs": {
            "type": "int",
            "column": "receiving_touchdowns"
        },
        "longest reception": {
            "type": "int",
            "column": "longest_reception"
        },
        "two pt": {
            "type": "int",
            "column": "two_point_receptions"
        }
    }

    normalized_receiving_stats = normalize_stat_list(stat_list, receiving_mapping)

    return normalized_receiving_stats