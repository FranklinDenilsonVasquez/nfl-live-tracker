from database.wrapper.game import normalize_game_response
from database.normalizers.receiving import normalize_receiving_stats
from tests.test_data.sample_receiving import sample_receiving_data
from pprint import pprint

def test_receiving_normalizer():
    normalized_receiving_stats = normalize_game_response(sample_receiving_data, "receiving",
                                                         normalize_receiving_stats)

    pprint(normalized_receiving_stats, sort_dicts=False, indent=4)

    assert isinstance(normalized_receiving_stats, list)
    assert len(normalized_receiving_stats) == 15

    sutton = next(p for p in normalized_receiving_stats if p["player_id"] == 2013)
    assert sutton["receiving_targets"] == 10
    assert sutton["total_receptions"] == 8
    assert sutton["receiving_yards"] == 97
    assert sutton["receiving_average"] == 12.1
    assert sutton["receiving_touchdowns"] == 0
    assert sutton["longest_reception"] == 34
    assert sutton["two_point_receptions"] == 0

    gordon = next(p for p in normalized_receiving_stats if p["player_id"] == 2003)
    assert gordon["receiving_targets"] == 6
    assert gordon["total_receptions"] == 5
    assert gordon["receiving_yards"] == 29
    assert gordon["receiving_average"] == 5.8
    assert gordon["receiving_touchdowns"] == 0
    assert gordon["longest_reception"] == 22
    assert gordon["two_point_receptions"] == 0

    hinton = next(p for p in normalized_receiving_stats if p["player_id"] == 2008)
    assert hinton["receiving_targets"] == 1
    assert hinton["total_receptions"] == 1
    assert hinton["receiving_yards"] == 27
    assert hinton["receiving_average"] == 27.0
    assert hinton["receiving_touchdowns"] == 0
    assert hinton["longest_reception"] == 27
    assert hinton["two_point_receptions"] == 0

    jeudy = next(p for p in normalized_receiving_stats if p["player_id"] == 2009)
    assert jeudy["receiving_targets"] == 7
    assert jeudy["total_receptions"] == 2
    assert jeudy["receiving_yards"] == 17
    assert jeudy["receiving_average"] == 8.5
    assert jeudy["receiving_touchdowns"] == 0
    assert jeudy["longest_reception"] == 16
    assert jeudy["two_point_receptions"] == 0

    okwuegbunam = next(p for p in normalized_receiving_stats if p["player_id"] == 2019)
    assert okwuegbunam["receiving_targets"] == 2
    assert okwuegbunam["total_receptions"] == 1
    assert okwuegbunam["receiving_yards"] == 12
    assert okwuegbunam["receiving_average"] == 12.0
    assert okwuegbunam["receiving_touchdowns"] == 0
    assert okwuegbunam["longest_reception"] == 12
    assert okwuegbunam["two_point_receptions"] == 0

    williams = next(p for p in normalized_receiving_stats if p["player_id"] == 2005)
    assert williams["receiving_targets"] == 5
    assert williams["total_receptions"] == 3
    assert williams["receiving_yards"] == 2
    assert williams["receiving_average"] == 0.7
    assert williams["receiving_touchdowns"] == 0
    assert williams["longest_reception"] == 2
    assert williams["two_point_receptions"] == 0

    saubert = next(p for p in normalized_receiving_stats if p["player_id"] == 2020)
    assert saubert["receiving_targets"] == 1
    assert saubert["total_receptions"] == 0
    assert saubert["receiving_yards"] == 0
    assert saubert["receiving_average"] == 0.0
    assert saubert["receiving_touchdowns"] == 0
    assert saubert["longest_reception"] == 0
    assert saubert["two_point_receptions"] == 0

    boone = next(p for p in normalized_receiving_stats if p["player_id"] == 2001)
    assert boone["receiving_targets"] == 1
    assert boone["total_receptions"] == 0
    assert boone["receiving_yards"] == 0
    assert boone["receiving_average"] == 0.0
    assert boone["receiving_touchdowns"] == 0
    assert boone["longest_reception"] == 0
    assert boone["two_point_receptions"] == 0

    samuel = next(p for p in normalized_receiving_stats if p["player_id"] == 991)
    assert samuel["receiving_targets"] == 7
    assert samuel["total_receptions"] == 5
    assert samuel["receiving_yards"] == 73
    assert samuel["receiving_average"] == 14.6
    assert samuel["receiving_touchdowns"] == 0
    assert samuel["longest_reception"] == 32
    assert samuel["two_point_receptions"] == 0

    aiyuk = next(p for p in normalized_receiving_stats if p["player_id"] == 987)
    assert aiyuk["receiving_targets"] == 8
    assert aiyuk["total_receptions"] == 3
    assert aiyuk["receiving_yards"] == 39
    assert aiyuk["receiving_average"] == 13.0
    assert aiyuk["receiving_touchdowns"] == 1
    assert aiyuk["longest_reception"] == 20
    assert aiyuk["two_point_receptions"] == 0

    wilson = next(p for p in normalized_receiving_stats if p["player_id"] == 985)
    assert wilson["receiving_targets"] == 3
    assert wilson["total_receptions"] == 3
    assert wilson["receiving_yards"] == 31
    assert wilson["receiving_average"] == 10.3
    assert wilson["receiving_touchdowns"] == 0
    assert wilson["longest_reception"] == 16
    assert wilson["two_point_receptions"] == 0
    assert wilson["team_id"] == 14
    assert wilson["player_name"] == "Jeff Wilson Jr."

    kittle = next(p for p in normalized_receiving_stats if p["player_id"] == 996)
    assert kittle["receiving_targets"] == 5
    assert kittle["total_receptions"] == 4
    assert kittle["receiving_yards"] == 28
    assert kittle["receiving_average"] == 7.0
    assert kittle["receiving_touchdowns"] == 0
    assert kittle["longest_reception"] == 11
    assert kittle["two_point_receptions"] == 0
    assert kittle["team_id"] == 14
    assert kittle["player_name"] == "George Kittle"

    juszczyk = next(p for p in normalized_receiving_stats if p["player_id"] == 986)
    assert juszczyk["receiving_targets"] == 1
    assert juszczyk["total_receptions"] == 1
    assert juszczyk["receiving_yards"] == 24
    assert juszczyk["receiving_average"] == 24.0
    assert juszczyk["receiving_touchdowns"] == 0
    assert juszczyk["longest_reception"] == 24
    assert juszczyk["two_point_receptions"] == 0
    assert juszczyk["team_id"] == 14
    assert juszczyk["player_name"] == "Kyle Juszczyk"

    mccloud = next(p for p in normalized_receiving_stats if p["player_id"] == 990)
    assert mccloud["receiving_targets"] == 1
    assert mccloud["total_receptions"] == 1
    assert mccloud["receiving_yards"] == 11
    assert mccloud["receiving_average"] == 11.0
    assert mccloud["receiving_touchdowns"] == 0
    assert mccloud["longest_reception"] == 11
    assert mccloud["two_point_receptions"] == 0
    assert mccloud["team_id"] == 14
    assert mccloud["player_name"] == "Ray-Ray McCloud III"

    jennings = next(p for p in normalized_receiving_stats if p["player_id"] == 989)
    assert jennings["receiving_targets"] == 3
    assert jennings["total_receptions"] == 1
    assert jennings["receiving_yards"] == 5
    assert jennings["receiving_average"] == 5.0
    assert jennings["receiving_touchdowns"] == 0
    assert jennings["longest_reception"] == 5
    assert jennings["two_point_receptions"] == 0
    assert jennings["team_id"] == 14
    assert jennings["player_name"] == "Jauan Jennings"

    print("Passed all the receiving unit tests!")

if __name__ == "__main__":
    test_receiving_normalizer()