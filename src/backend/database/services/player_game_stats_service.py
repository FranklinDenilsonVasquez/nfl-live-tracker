# Orchestration logic for player game stats
from src.backend.database.wrapper.game import normalize_game_response
from src.backend.database.normalizers.defense import normalize_defense_stats
from src.backend.database.normalizers.fumbles import normalize_fumbles_stats
from src.backend.database.normalizers.interceptions import normalize_interception_stats
from src.backend.database.normalizers.kick_retruns import normalize_kick_return_stats
from src.backend.database.normalizers.kicking import normalize_kicking_stats
from src.backend.database.normalizers.passing import normalize_passing_stats
from src.backend.database.normalizers.punt_returns import normalize_punt_return_stats
from src.backend.database.normalizers.punting import normalize_punting_stats
from src.backend.database.normalizers.receiving import normalize_receiving_stats
from src.backend.database.normalizers.rushing import normalize_rushing_stats
from pprint import pprint

stat_groups = [
    ("defensive", normalize_defense_stats),
    ("fumbles", normalize_fumbles_stats),
    ("interceptions", normalize_interception_stats),
    ("kick_returns", normalize_kick_return_stats),
    ("kicking", normalize_kicking_stats),
    ("passing", normalize_passing_stats),
    ("punt_returns", normalize_punt_return_stats),
    ("punting", normalize_punting_stats),
    ("receiving", normalize_receiving_stats),
    ("rushing", normalize_rushing_stats)
]

def orchestrate_player_game_stats(game_response, game_id=None):
    grouped_stats = {}

    for group, normalized_func in stat_groups:
        stats = normalize_game_response(
                    game_response,
                    group,
                    normalized_func,
                    game_id
                    )
        print(f"Added group = {group}")

        grouped_stats[group] = stats
    return grouped_stats

from src.backend.database.inserts.defense import insert_defense_player_stat
from src.backend.database.inserts.fumbles import insert_fumble_player_stats
from src.backend.database.inserts.interceptions import insert_interception_player_stats
from src.backend.database.inserts.kick_retruns import insert_kick_return_player_stats
from src.backend.database.inserts.kicking import insert_kicking_player_stats
from src.backend.database.inserts.passing import insert_player_passing_stats
from src.backend.database.inserts.punt_returns import insert_punt_return_player_stats
from src.backend.database.inserts.punting import insert_punting_player_stats
from src.backend.database.inserts.receiving import insert_receiving_player_stats
from src.backend.database.inserts.rushing import insert_rushing_player_stats
from src.backend.database.repositories.player_repository import get_player_map_for_stats
from src.backend.utils.logging import logger

def process_player_game_stats(conn, game_response, game_id=None):
    logger.info("Starting player game stat ingestion")

    grouped_stats = orchestrate_player_game_stats(game_response, game_id)

    all_stats_flat = []
    for stats_list in grouped_stats.values():
        if stats_list:
            all_stats_flat.extend(stats_list)

    try:
        with conn.cursor() as cursor:
            player_map = get_player_map_for_stats(cursor, all_stats_flat)

            insert_defense_player_stat(cursor, grouped_stats["defensive"], player_map)
            insert_fumble_player_stats(cursor, grouped_stats["fumbles"], player_map)
            insert_interception_player_stats(cursor, grouped_stats["interceptions"], player_map)
            insert_kick_return_player_stats(cursor, grouped_stats["kick_returns"], player_map)
            insert_kicking_player_stats(cursor, grouped_stats["kicking"], player_map)
            insert_player_passing_stats(cursor, grouped_stats["passing"], player_map)
            insert_punt_return_player_stats(cursor, grouped_stats["punt_returns"], player_map)
            insert_punting_player_stats(cursor, grouped_stats["punting"], player_map)
            insert_receiving_player_stats(cursor, grouped_stats["receiving"], player_map)
            insert_rushing_player_stats(cursor, grouped_stats["rushing"], player_map)

            conn.commit()
            logger.info("Successfully inserted all player game stats")
    except Exception:
        conn.rollback()
        logger.exception("Player game stat ingestion failed")
        raise