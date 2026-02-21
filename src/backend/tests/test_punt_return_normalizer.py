from database.wrapper.game import normalize_game_response
from database.normalizers.punt_returns import normalize_punt_return_stats
from tests.test_data.sample_punt_returns import sample_punt_return_data
from pprint import pprint

def test_punt_returns_normalizer():
    normalized_punt_returns = normalize_game_response(sample_punt_return_data, "punt_returns",
                                                      normalize_punt_return_stats)

    pprint(normalized_punt_returns)

    assert isinstance(normalized_punt_returns, list)

    washington = next(p for p in normalized_punt_returns if p["player_id"] == 2015)
    assert washington["total"] == 1
    assert washington["yards"] == 9
    assert washington["average"] == 9.0
    assert washington["long"] == 9
    assert washington["touchdown"] == 0

    McCloud = next(p for p in normalized_punt_returns if p["player_id"] == 990)
    assert McCloud["total"] == 5
    assert McCloud["yards"] == 40
    assert McCloud["average"] == 8.0
    assert McCloud["long"] == 18
    assert McCloud["touchdown"] == 0

    print("All punt return unit tests passed!")



if __name__ == "__main__":
    test_punt_returns_normalizer()