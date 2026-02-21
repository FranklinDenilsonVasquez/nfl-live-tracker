from database.wrapper.game import normalize_game_response
from database.normalizers.interceptions import normalize_interception_stats
from tests.test_data.sample_interception import sample_interceptions_stats
from pprint import pprint

def test_interception_normalizer():
    normalized_interceptions = normalize_game_response(sample_interceptions_stats, "interceptions",
                                         normalize_interception_stats)

    pprint(normalized_interceptions)

    # ---- Top-level checks ----
    assert isinstance(normalized_interceptions, list)
    assert len(normalized_interceptions) == 2
    jonas = next(p for p in normalized_interceptions if p["player_id"] == 2051)
    assert jonas["total_interceptions"] == 1
    assert jonas["yards"] == 1
    assert jonas["intercepted_touch_downs"] == 0
    assert jonas["team_id"] == 28

    patrick = next(p for p in normalized_interceptions if p["player_id"] == 2055)
    assert patrick["total_interceptions"] == 2
    assert patrick["yards"] == 30
    assert patrick["intercepted_touch_downs"] == 1
    assert patrick["team_id"] == 28

    print("Passed all interceptions flat-list tests!")

if __name__ == "__main__":
    test_interception_normalizer()