from database.normalizers.defense import normalize_defense_stats
from tests.test_data.sample_defense import sample_defense_stats
from pprint import pprint

def test_defense_normalizer():
    normalized = normalize_defense_stats(sample_defense_stats)

    assert normalized["tackles"] == 10
    assert normalized["unassisted_tackles"] == 8
    assert normalized["sacks"] == 0
    assert normalized["tackles_for_loss"] == 0
    assert normalized["passes_defended"] == 0
    assert "unknown_stat" not in normalized

    # Edge case
    edge_case_stats = [
        {"name": "tackles", "value": ""},
        {"name": "sacks", "value": None},
        {"name": "unassisted tackles", "value": "—"},
        {"name": "unknown_stat", "value": "5"},
    ]

    normalized_edge = normalize_defense_stats(edge_case_stats)
    assert normalized_edge["tackles"] == 0
    assert normalized_edge["unassisted_tackles"] == 0
    assert normalized_edge["sacks"] == 0
    assert "unknown_stat" not in normalized_edge

    print("All defense normalizer test passed!")
    pprint(normalized)
    pprint(normalized_edge)

if __name__ == "__main__":
    test_defense_normalizer()