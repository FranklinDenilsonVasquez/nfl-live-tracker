# Orchestration logic for player game stats
from database.wrapper.game import normalize_game_response
from database.normalizers.defense import normalize_defense_stats
from database.normalizers.fumbles import normalize_fumbles_stats
from database.normalizers.interceptions import normalize_interception_stats
from database.normalizers.kick_retruns import normalize_kick_return_stats
from database.normalizers.kicking import normalize_kicking_stats
from database.normalizers.passing import normalize_passing_stats
from database.normalizers.punt_returns import normalize_punt_return_stats
from database.normalizers.punting import normalize_punting_stats
from database.normalizers.receiving import normalize_receiving_stats
from database.normalizers.rushing import normalize_rushing_stats
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
    all_normalized_stats = []

    for group, normalized_func in stat_groups:
        stats = normalize_game_response(
                    game_response,
                    group,
                    normalized_func,
                    game_id
                    )
        print(f"Added group = {group}")

        all_normalized_stats.extend(stats)
        # print(len(all_normalized_stats))
    return all_normalized_stats

