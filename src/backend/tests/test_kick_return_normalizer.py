from database.wrapper.defense import normalize_game_response
from database.normalizers.kick_retruns import normalize_kick_return_stats
from tests.test_data.sample_kick_return import sample_kick_return_stats
from pprint import pprint
import json

def test_kick_return_normalizer():
    normalized_kick_returns = normalize_game_response(sample_kick_return_stats, "kick_returns",
                                                      normalize_kick_return_stats)

    pprint(normalized_kick_returns, sort_dicts=False)

    assert isinstance(normalized_kick_returns, list)
    assert len(normalized_kick_returns) == 2

    washington = next(p for p in normalized_kick_returns if p["player_id"] == 2015)
    assert washington["total_kick_returns"] == 1
    assert washington["kick_return_yards"] == 14
    assert washington["kick_return_average"] == 14.0
    assert washington["kick_return_long"] == 14
    assert washington["td"] == 0
    assert washington["kick_return_td"] == 0
    assert washington["exp_return_td"] == 0

    McCloud = next(p for p in normalized_kick_returns if p["player_id"] == 990)
    assert McCloud["total_kick_returns"] == 2
    assert McCloud["kick_return_yards"] == 23
    assert McCloud["kick_return_average"] == 11.5
    assert McCloud["kick_return_long"] == 15
    assert McCloud["td"] == 0
    assert McCloud["kick_return_td"] == 0
    assert McCloud["exp_return_td"] == 0

    print("Passed all kick return flat list test!")


if __name__ == "__main__":
    test_kick_return_normalizer()