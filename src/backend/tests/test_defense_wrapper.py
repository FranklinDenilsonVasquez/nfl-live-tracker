from database.wrapper.defense import normalize_defense_game_response


def test_defense_wrapper():
    sample_defense_stats = {
        "team": {
            "id": 32,
            "name": "Minnesota Vikings",
            "logo": "https://media.api-sports.io/american-football/teams/32.png"
        },
        "groups": [
            {
                "name": "Defensive",
                "players": [
                    {
                        "player": {
                            "id": 3295,
                            "name": "Holton Hill",
                            "image": "https://media.api-sports.io/american-football/players/3295.png"
                        },
                        "statistics": [
                            {"name": "tackles", "value": "4"},
                            {"name": "unassisted tackles", "value": "4"},
                            {"name": "sacks", "value": "0"},
                            {"name": "tfl", "value": "0"},
                            {"name": "passes defended", "value": "1"},
                            {"name": "qb hts", "value": "0"},
                            {"name": "interceptions for touch downs", "value": "0"},
                            {"name": "blocked kicks", "value": "0"},
                            {"name": "kick return td", "value": "0"},
                            {"name": "exp return td", "value": "0"},
                            {"name": "ff", "value": None},
                        ],
                    },
                    {
                        "player": {
                            "id": 4127,
                            "name": "Kentrell Brothers",
                            "image": "https://media.api-sports.io/american-football/players/4127.png"
                        },
                        "statistics": [
                            {"name": "tackles", "value": "4"},
                            {"name": "unassisted tackles", "value": "2"},
                            {"name": "sacks", "value": "0"},
                            {"name": "tfl", "value": "0"},
                            {"name": "passes defended", "value": "1"},
                            {"name": "qb hts", "value": "0"},
                            {"name": "interceptions for touch downs", "value": "0"},
                            {"name": "blocked kicks", "value": "0"},
                            {"name": "kick return td", "value": "0"},
                            {"name": "exp return td", "value": "0"},
                            {"name": "ff", "value": None},
                        ],
                    },
                    {
                        "player": {
                            "id": 4120,
                            "name": "Reshard Cliett",
                            "image": "https://media.api-sports.io/american-football/players/4120.png"
                        },
                        "statistics": [
                            {"name": "tackles", "value": "4"},
                            {"name": "unassisted tackles", "value": "1"},
                            {"name": "sacks", "value": "0"},
                            {"name": "tfl", "value": "0"},
                            {"name": "passes defended", "value": "0"},
                            {"name": "qb hts", "value": "0"},
                            {"name": "interceptions for touch downs", "value": "0"},
                            {"name": "blocked kicks", "value": "0"},
                            {"name": "kick return td", "value": "0"},
                            {"name": "exp return td", "value": "0"},
                            {"name": "ff", "value": None},
                        ],
                    },
                ],
            }
        ],
    }

    normalized = normalize_defense_game_response([sample_defense_stats])
    # number of players in the response
    length = len(normalized)
    assert len(normalized) == 3
    for player in normalized:
        assert isinstance(player, dict)
        assert "player_id" in player
        assert "team_id" in player

    # Test the values for one player (Reshard Cliett)
    player_4120 = next(p for p in normalized if p["player_id"] == 4120)
    assert player_4120["team_id"] == 32
    assert player_4120["tackles"] == 4
    assert player_4120["unassisted_tackles"] == 1
    assert player_4120["sacks"] == 0
    assert player_4120["tackles_for_loss"] == 0
    assert player_4120["passes_defended"] == 0
    assert player_4120["qb_hits"] == 0
    assert player_4120["interceptions_for_tds"] == 0
    assert player_4120["blocked_kicks"] == 0
    assert player_4120["kick_return_td"] == 0
    assert player_4120["expected_return_td"] == 0
    assert player_4120["forced_fumbles"] == 0

    print("All defense normalizer test passed!")

if __name__ == "__main__":
    test_defense_wrapper()