from database.wrapper.defense import normalize_game_response
from database.normalizers.passing import normalize_passing_stats
from tests.test_data.sample_passing import sample_passing_data
from pprint import pprint

def test_passing_normalizer():
    passing_normalized = normalize_game_response(sample_passing_data, "passing",
                                                 normalize_passing_stats)

    pprint(passing_normalized)

    assert isinstance(passing_normalized, list)
    assert len(passing_normalized) == 2

    wilson = next(p for p in passing_normalized if p["player_id"] == 2000)
    assert wilson["passing_completion"] == 20
    assert wilson["passing_attempted"] == 33
    assert wilson["passing_yards"] == 184
    assert wilson["passing_average"] == 5.6
    assert wilson["passing_touch_downs"] == 0
    assert wilson["passing_interceptions"] == 0
    assert wilson["sacks_total"] == 4
    assert wilson["sacks_yards"] == 24
    assert wilson["passer_rating"] == 32.9
    assert wilson["two_point_conversions"] == 0

    garoppolo = next(p for p in passing_normalized if p["player_id"] == 977)
    assert garoppolo["passing_completion"] == 18
    assert garoppolo["passing_attempted"] == 29
    assert garoppolo["passing_yards"] == 211
    assert garoppolo["passing_average"] == 7.3
    assert garoppolo["passing_touch_downs"] == 1
    assert garoppolo["passing_interceptions"] == 1
    assert garoppolo["sacks_total"] == 4
    assert garoppolo["sacks_yards"] == 32
    assert garoppolo["passer_rating"] == 14.2
    assert garoppolo["two_point_conversions"] == 0

    print("Passed all passing unit tests!")


if __name__ == "__main__":
    test_passing_normalizer()