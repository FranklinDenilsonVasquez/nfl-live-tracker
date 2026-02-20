from database.wrapper.defense import normalize_game_response
from database.normalizers.kicking import normalize_kicking_stats
from tests.test_data.sample_kicking import sample_kicking_data
from pprint import pprint

def test_kicking_normalizer():
    normalized_kicking= normalize_game_response(sample_kicking_data,"kicking",
                                                normalize_kicking_stats)

    pprint(normalized_kicking)


if __name__ == "__main__":
    test_kicking_normalizer()