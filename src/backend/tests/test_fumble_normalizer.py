from database.wrapper.defense import normalize_game_response
from database.normalizers.fumbles import normalize_fumbles_stats
from tests.test_data.sample_fumbles import sample_fumbles_stats

def test_fumble_normalizer():
    normalized = normalize_game_response(sample_fumbles_stats, "fumbles", normalize_fumbles_stats)

    print(normalized)

    # ---- Flat list checks ----
    assert isinstance(normalized, list)
    assert len(normalized) == 7  # total players

    # ---- Denver Broncos players ----
    melvin = next(p for p in normalized if p["player_id"] == 2003)
    assert melvin["total_fumbles"] == 2
    assert melvin["fumble_lost"] == 0
    assert melvin["fumble_recovery"] == 1
    assert melvin["fumble_recovery_td"] == 0
    assert melvin["team_id"] == 28

    kareem = next(p for p in normalized if p["player_id"] == 2067)
    assert kareem["total_fumbles"] == 0
    assert kareem["fumble_recovery"] == 1

    # ---- San Francisco 49ers players ----
    jimmy = next(p for p in normalized if p["player_id"] == 977)
    assert jimmy["total_fumbles"] == 1
    assert jimmy["fumble_lost"] == 1
    assert jimmy["team_id"] == 14

    jeff = next(p for p in normalized if p["player_id"] == 985)
    assert jeff["total_fumbles"] == 1
    assert jeff["fumble_lost"] == 1

    ray = next(p for p in normalized if p["player_id"] == 990)
    assert ray["total_fumbles"] == 1
    assert ray["fumble_lost"] == 0
    assert ray["fumble_recovery"] == 1

    print("Passed all fumble normalizer tests!")

if __name__ == "__main__":
    test_fumble_normalizer()