BASELINE_RATING = 6.0
RATING_MIN = 0.0
RATING_MAX = 10.0

_SKILL_STAT_WEIGHTS = {
    "total_receptions": 0.05,
    "receiving_yards": 0.015,
    "receiving_touchdowns": 0.7,
    "rushing_yards": 0.015,
    "rushing_touchdowns": 0.7,
    "fumble_lost": -0.8,
}

_SKILL_EFFICIENCY = [
    {
        "type": "completion_rate",
        "volume_field": "receiving_targets",
        "success_field": "total_receptions",
        "min_volume": 3,
        "baseline_rate": 0.65,
        "weight": 0.05,
        "volume_scaled": True,
    },
    {
        "type": "yards_per_unit",
        "volume_field": "total_rushes",
        "yards_field": "rushing_yards",
        "min_volume": 5,
        "baseline_avg": 4.0,
        "weight": 0.03,
    },
]

_DEFENSE_STAT_WEIGHTS = {
    "tackles": 0.1,
    "unassisted_tackles": 0.05,
    "tackles_for_loss": 0.3,
    "sacks": 0.9,
    "qb_hits": 0.2,
    "passes_defended": 0.3,
    "forced_fumbles": 0.7,
    "fumble_recovery": 0.6,
    "fumble_recovery_td": 1.5,
    "total_interceptions": 1.2,
    "intercepted_touch_downs": 1.5,
    "blocked_kicks": 1.0,
    "kick_return_td": 1.5,
    "expected_return_td": 1.5,
    "fumble_lost": -0.8,
}

# Position -> weight config for Player Game Rating (see CONTEXT.md, docs/adr/0001).
# Only positions listed here are in the v1 rating scope; KR, PR, G, OT are
# deliberately absent (see docs/adr/0001-absolute-baseline-player-game-rating.md).
POSITION_RATING_CONFIG = {
    "QB": {
        "stat_weights": {
            "passing_yards": 0.005,
            "passing_touch_downs": 0.3,
            "passing_interceptions": -0.8,
            "sacks_total": -0.15,
            "rushing_yards": 0.02,
            "rushing_touchdowns": 0.6,
            "fumble_lost": -0.8,
        },
        "efficiency": [
            {
                "type": "completion_rate",
                "volume_field": "passing_attempted",
                "success_field": "passing_completion",
                "min_volume": 10,
                "baseline_rate": 0.60,
                "weight": 0.03,
                "volume_scaled": False,
            },
        ],
    },
    "RB": {"stat_weights": _SKILL_STAT_WEIGHTS, "efficiency": _SKILL_EFFICIENCY},
    "FB": {"stat_weights": _SKILL_STAT_WEIGHTS, "efficiency": _SKILL_EFFICIENCY},
    "WR": {"stat_weights": _SKILL_STAT_WEIGHTS, "efficiency": _SKILL_EFFICIENCY},
    "TE": {"stat_weights": _SKILL_STAT_WEIGHTS, "efficiency": _SKILL_EFFICIENCY},
    "DE": {"stat_weights": _DEFENSE_STAT_WEIGHTS, "efficiency": []},
    "DT": {"stat_weights": _DEFENSE_STAT_WEIGHTS, "efficiency": []},
    "LB": {"stat_weights": _DEFENSE_STAT_WEIGHTS, "efficiency": []},
    "CB": {"stat_weights": _DEFENSE_STAT_WEIGHTS, "efficiency": []},
    "S": {"stat_weights": _DEFENSE_STAT_WEIGHTS, "efficiency": []},
    "DB": {"stat_weights": _DEFENSE_STAT_WEIGHTS, "efficiency": []},
    "PK": {
        "stat_weights": {
            "field_goals_from_1_19_yards": 0.5,
            "field_goals_from_20_29_yards": 0.5,
            "field_goals_from_30_39_yards": 0.5,
            "field_goals_from_40_49_yards": 0.6,
            "field_goals_from_50_yards": 0.7,
            "xp_made": 0.1,
        },
        "efficiency": [],
    },
    "P": {
        "stat_weights": {
            "inside_20": 0.3,
            "touchbacks": -0.2,
        },
        "efficiency": [
            {
                "type": "yards_per_unit",
                "volume_field": "punt_total",
                "yards_field": "punt_yards",
                "min_volume": 1,
                "baseline_avg": 45.0,
                "weight": 0.1,
            },
        ],
    },
}
