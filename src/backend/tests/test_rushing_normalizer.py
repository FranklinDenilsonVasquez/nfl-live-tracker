from database.wrapper.game import normalize_game_response
from database.normalizers.rushing import normalize_rushing_stats
from tests.test_data.sample_rushing import sample_rushing_data
from pprint import pprint

def test_rushing_normalizer():
    normalized_rushing_stats = normalize_game_response(sample_rushing_data, "rushing",
                                                       normalize_rushing_stats)

    pprint(normalized_rushing_stats, sort_dicts=False, indent=4)

    # Denver Broncos players
    javonte = next(p for p in normalized_rushing_stats if p["player_id"] == 2005)
    assert javonte["total_rushes"] == 15
    assert javonte["rushing_yards"] == 58
    assert javonte["rushing_average"] == 3.9
    assert javonte["rushing_touchdowns"] == 0
    assert javonte["longest_rush"] == 16
    assert javonte["two_point_rushes"] == 0
    assert javonte["kick_return_touchdowns"] == 0
    assert javonte["exp_return_touchdowns"] == 0

    gordon = next(p for p in normalized_rushing_stats if p["player_id"] == 2003)
    assert gordon["total_rushes"] == 12
    assert gordon["rushing_yards"] == 26
    assert gordon["rushing_average"] == 2.2
    assert gordon["rushing_touchdowns"] == 1
    assert gordon["longest_rush"] == 6
    assert gordon["two_point_rushes"] == 0
    assert gordon["kick_return_touchdowns"] == 0
    assert gordon["exp_return_touchdowns"] == 0

    wilson = next(p for p in normalized_rushing_stats if p["player_id"] == 2000)
    assert wilson["total_rushes"] == 6
    assert wilson["rushing_yards"] == 17
    assert wilson["rushing_average"] == 2.8
    assert wilson["rushing_touchdowns"] == 0
    assert wilson["longest_rush"] == 12
    assert wilson["two_point_rushes"] == 0
    assert wilson["kick_return_touchdowns"] == 0
    assert wilson["exp_return_touchdowns"] == 0

    # San Francisco 49ers players
    jeff = next(p for p in normalized_rushing_stats if p["player_id"] == 985)
    assert jeff["total_rushes"] == 12
    assert jeff["rushing_yards"] == 75
    assert jeff["rushing_average"] == 6.3
    assert jeff["rushing_touchdowns"] == 0
    assert jeff["longest_rush"] == 37
    assert jeff["two_point_rushes"] == 0
    assert jeff["kick_return_touchdowns"] == 0
    assert jeff["exp_return_touchdowns"] == 0

    mason = next(p for p in normalized_rushing_stats if p["player_id"] == 983)
    assert mason["total_rushes"] == 1
    assert mason["rushing_yards"] == 7
    assert mason["rushing_average"] == 7.0
    assert mason["rushing_touchdowns"] == 0
    assert mason["longest_rush"] == 7
    assert mason["two_point_rushes"] == 0
    assert mason["kick_return_touchdowns"] == 0
    assert mason["exp_return_touchdowns"] == 0

    samuel = next(p for p in normalized_rushing_stats if p["player_id"] == 991)
    assert samuel["total_rushes"] == 5
    assert samuel["rushing_yards"] == 6
    assert samuel["rushing_average"] == 1.2
    assert samuel["rushing_touchdowns"] == 0
    assert samuel["longest_rush"] == 3
    assert samuel["two_point_rushes"] == 0
    assert samuel["kick_return_touchdowns"] == 0
    assert samuel["exp_return_touchdowns"] == 0

    garoppolo = next(p for p in normalized_rushing_stats if p["player_id"] == 977)
    assert garoppolo["total_rushes"] == 1
    assert garoppolo["rushing_yards"] == 0
    assert garoppolo["rushing_average"] == 0.0
    assert garoppolo["rushing_touchdowns"] == 0
    assert garoppolo["longest_rush"] == 0
    assert garoppolo["two_point_rushes"] == 0
    assert garoppolo["kick_return_touchdowns"] == 0
    assert garoppolo["exp_return_touchdowns"] == 0

    print("Passed all rushing unit tests!")

if __name__ == "__main__":
    test_rushing_normalizer()