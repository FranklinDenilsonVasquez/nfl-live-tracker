from src.backend.core.rating_config import (
    POSITION_RATING_CONFIG,
    BASELINE_RATING,
    RATING_MIN,
    RATING_MAX,
)


def _num(stats: dict, field: str) -> float:
    # Postgres DECIMAL columns come back as decimal.Decimal via psycopg2,
    # which can't be multiplied with the plain floats in rating_config.py.
    return float(stats.get(field) or 0)


def _stat_weight_delta(stats: dict, stat_weights: dict) -> float:
    return sum(
        weight * _num(stats, field)
        for field, weight in stat_weights.items()
    )


def _completion_rate_delta(stats: dict, cfg: dict) -> float:
    volume = _num(stats, cfg["volume_field"])
    if volume < cfg["min_volume"]:
        return 0.0

    success = _num(stats, cfg["success_field"])
    diff = (success / volume) - cfg["baseline_rate"]

    if cfg["volume_scaled"]:
        return diff * volume * cfg["weight"]
    return diff * 100 * cfg["weight"]


def _yards_per_unit_delta(stats: dict, cfg: dict) -> float:
    volume = _num(stats, cfg["volume_field"])
    if volume < cfg["min_volume"]:
        return 0.0

    yards = _num(stats, cfg["yards_field"])
    diff = (yards / volume) - cfg["baseline_avg"]
    return diff * volume * cfg["weight"]


_EFFICIENCY_HANDLERS = {
    "completion_rate": _completion_rate_delta,
    "yards_per_unit": _yards_per_unit_delta,
}


def _kicker_miss_delta(stats: dict) -> float:
    fg_made = _num(stats, "fg_made")
    fg_attempted = _num(stats, "fg_attempted")
    xp_made = _num(stats, "xp_made")
    xp_attempted = _num(stats, "xp_attempted")

    return (
        (fg_attempted - fg_made) * -0.6
        + (xp_attempted - xp_made) * -0.4
    )


def compute_game_rating(position: str, stats: dict) -> float | None:
    """Compute a Player Game Rating (see CONTEXT.md) for one player's single-game stat line.

    `stats` is a flat dict of raw stat field names (e.g. passing_yards,
    total_receptions, tackles) to values, scoped to one player's one game.
    Fields the player's position doesn't use are ignored.

    Returns None for positions outside the v1 rating scope (not present in
    POSITION_RATING_CONFIG - e.g. KR, PR, G, OT).
    """
    config = POSITION_RATING_CONFIG.get(position)
    if config is None:
        return None

    delta = _stat_weight_delta(stats, config["stat_weights"])

    for efficiency_cfg in config["efficiency"]:
        handler = _EFFICIENCY_HANDLERS[efficiency_cfg["type"]]
        delta += handler(stats, efficiency_cfg)

    if position == "PK":
        delta += _kicker_miss_delta(stats)

    rating = max(RATING_MIN, min(RATING_MAX, BASELINE_RATING + delta))
    return round(rating, 1)
