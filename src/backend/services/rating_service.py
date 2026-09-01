# Orchestration logic for Player Game Rating (see CONTEXT.md, docs/adr/0001)
from src.backend.core.player_rating import compute_game_rating
from src.backend.database.repositories.player_repository import get_player_position_map
from src.backend.database.inserts.rating import upsert_player_game_ratings
from src.backend.utils.logging import logger


def _merge_stats_by_player_game(grouped_stats):
    merged = {}

    for stats_list in grouped_stats.values():
        for row in stats_list:
            api_player_id = row.get("player_id")
            game_id = row.get("game_id")
            if api_player_id is None or game_id is None:
                continue

            key = (api_player_id, game_id)
            merged.setdefault(key, {}).update(row)

    return merged


def compute_and_store_ratings(cursor, grouped_stats, player_map):
    merged_stats = _merge_stats_by_player_game(grouped_stats)
    if not merged_stats:
        return

    internal_player_ids = {
        player_map[api_player_id]
        for (api_player_id, _game_id) in merged_stats
        if api_player_id in player_map
    }
    position_map = get_player_position_map(cursor, internal_player_ids)

    rating_values = []
    for (api_player_id, game_id), stats in merged_stats.items():
        internal_player_id = player_map.get(api_player_id)
        if not internal_player_id:
            logger.warning(f"Unknown player (player_id : {api_player_id}), skipping rating.")
            continue

        position = position_map.get(internal_player_id)
        if not position:
            continue

        rating = compute_game_rating(position, stats)
        if rating is None:
            continue

        rating_values.append((internal_player_id, game_id, rating))

    upsert_player_game_ratings(cursor, rating_values)
