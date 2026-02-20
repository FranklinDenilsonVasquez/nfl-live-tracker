from .utils import normalize_stat_list

def normalize_kicking_stats(stat_line):
    kicking_mapping = {
        "field goals" : {
            "type" : "ratio",
            "columns" : ("fg_made", "fg_attempted")
        },
        "pct" : {
            "type" : "float",
            "column" : "fg_percentage"
        },
        "long" : {
            "type" : "int",
            "column" : "long"
        },
        "extra point": {
            "type" : "ratio",
            "columns" : ("xp_made", "xp_attempted")
        },
        "points" : {
            "type" : "int",
            "column" : "points"
        },
        "field goals from 1 19 yards" : {
            "type" : "int",
            "column" : "field_goals_from_1_19_yards"
        },
        "field goals from 20 29 yards": {
            "type": "int",
            "column": "field_goals_from_20_29_yards"
        },
        "field goals from 30 39 yards": {
            "type": "int",
            "column": "field_goals_from_30_39_yards"
        },
        "field goals from 40 49 yards": {
            "type": "int",
            "column": "field_goals_from_40_49_yards"
        },
        "field goals from 50 yards": {
            "type": "int",
            "column": "field_goals_from_50_yards"
        }
    }

    normalized_kicking = normalize_stat_list(stat_line, kicking_mapping)

    return normalized_kicking