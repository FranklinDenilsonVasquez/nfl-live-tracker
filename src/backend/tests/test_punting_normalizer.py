from database.wrapper.game import normalize_game_response
from database.normalizers.punting import normalize_punting_stats
from tests.test_data.sample_punting import sample_punting_data
from pprint import pprint

def test_punting_normalizer():
    normalized_punting_stats = normalize_game_response(sample_punting_data, "punting",
                                                       normalize_punting_stats)

    pprint(normalized_punting_stats)

    assert isinstance(normalized_punting_stats, list)
    assert len(normalized_punting_stats) == 2

    waitman = next(p for p in normalized_punting_stats if p["player_id"] == 2073)
    assert waitman["punt_total"] == 10
    assert waitman["punt_yards"] == 476
    assert waitman["punt_average"] == 47.6
    assert waitman["touchbacks"] == 0
    assert waitman["inside_20"] == 6
    assert waitman["long_punt"] == 57

    wishnowsky = next(p for p in normalized_punting_stats if p["player_id"] == 1046)
    assert wishnowsky["punt_total"] == 7
    assert wishnowsky["punt_yards"] == 362
    assert wishnowsky["punt_average"] == 51.7
    assert wishnowsky["touchbacks"] == 2
    assert wishnowsky["inside_20"] == 3
    assert wishnowsky["long_punt"] == 74

    print("Passed all punting unit tests!")

if __name__ == "__main__":
    test_punting_normalizer()