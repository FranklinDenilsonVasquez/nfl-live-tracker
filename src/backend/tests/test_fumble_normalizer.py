from database.wrapper.defense import normalize_game_response
from database.normalizers.fumbles import normalize_fumbles_stats

def test_fumble_normalizer():
    sample_fumbles_stats = [
        {
            "team": {
                "id": 28,
                "name": "Denver Broncos",
                "logo": "https://media.api-sports.io/american-football/teams/28.png"
            },
            "groups": [
                {
                    "name": "Fumbles",
                    "players": [
                        {
                            "player": {
                                "id": 2003,
                                "name": "Melvin Gordon III",
                                "image": "https://media.api-sports.io/american-football/players/2003.png"
                            },
                            "statistics": [
                                {"name": "total", "value": "2"},
                                {"name": "lost", "value": "0"},
                                {"name": "rec", "value": "1"},
                                {"name": "rec td", "value": "0"},
                            ],
                        },
                        {
                            "player": {
                                "id": 2067,
                                "name": "Kareem Jackson",
                                "image": "https://media.api-sports.io/american-football/players/2067.png"
                            },
                            "statistics": [
                                {"name": "total", "value": "0"},
                                {"name": "lost", "value": "0"},
                                {"name": "rec", "value": "1"},
                                {"name": "rec td", "value": "0"},
                            ],
                        },
                        {
                            "player": {
                                "id": 2000,
                                "name": "Russell Wilson",
                                "image": "https://media.api-sports.io/american-football/players/2000.png"
                            },
                            "statistics": [
                                {"name": "total", "value": "0"},
                                {"name": "lost", "value": "0"},
                                {"name": "rec", "value": "1"},
                                {"name": "rec td", "value": "0"},
                            ],
                        },
                        {
                            "player": {
                                "id": 2052,
                                "name": "Josey Jewell",
                                "image": "https://media.api-sports.io/american-football/players/2052.png"
                            },
                            "statistics": [
                                {"name": "total", "value": "0"},
                                {"name": "lost", "value": "0"},
                                {"name": "rec", "value": "1"},
                                {"name": "rec td", "value": "0"},
                            ],
                        },
                    ],
                }
            ],
        },
        {
            "team": {
                "id": 14,
                "name": "San Francisco 49ers",
                "logo": "https://media.api-sports.io/american-football/teams/14.png"
            },
            "groups": [
                {
                    "name": "Fumbles",
                    "players": [
                        {
                            "player": {
                                "id": 977,
                                "name": "Jimmy Garoppolo",
                                "image": "https://media.api-sports.io/american-football/players/977.png"
                            },
                            "statistics": [
                                {"name": "total", "value": "1"},
                                {"name": "lost", "value": "1"},
                                {"name": "rec", "value": "0"},
                                {"name": "rec td", "value": "0"},
                            ],
                        },
                        {
                            "player": {
                                "id": 985,
                                "name": "Jeff Wilson Jr.",
                                "image": "https://media.api-sports.io/american-football/players/985.png"
                            },
                            "statistics": [
                                {"name": "total", "value": "1"},
                                {"name": "lost", "value": "1"},
                                {"name": "rec", "value": "0"},
                                {"name": "rec td", "value": "0"},
                            ],
                        },
                        {
                            "player": {
                                "id": 990,
                                "name": "Ray-Ray McCloud III",
                                "image": "https://media.api-sports.io/american-football/players/990.png"
                            },
                            "statistics": [
                                {"name": "total", "value": "1"},
                                {"name": "lost", "value": "0"},
                                {"name": "rec", "value": "1"},
                                {"name": "rec td", "value": "0"},
                            ],
                        },
                    ],
                }
            ],
        },
    ]

    normalized = normalize_game_response(sample_fumbles_stats, "fumbles", normalize_fumbles_stats)
    print(normalized)
    # ---- Flat list checks ----
    assert isinstance(normalized, list)
    assert len(normalized) == 7  # total players

    # ---- Denver Broncos players ----
    melvin = next(p for p in normalized if p["player_id"] == 2003)
    assert melvin["total_fumbles"] == 2
    assert melvin["fumble_lost"] == 0
    assert melvin["fumble_recovery"] == 1
    assert melvin["fumble_recovery_td"] == 0
    assert melvin["team_id"] == 28

    kareem = next(p for p in normalized if p["player_id"] == 2067)
    assert kareem["total_fumbles"] == 0
    assert kareem["fumble_recovery"] == 1

    # ---- San Francisco 49ers players ----
    jimmy = next(p for p in normalized if p["player_id"] == 977)
    assert jimmy["total_fumbles"] == 1
    assert jimmy["fumble_lost"] == 1
    assert jimmy["team_id"] == 14

    jeff = next(p for p in normalized if p["player_id"] == 985)
    assert jeff["total_fumbles"] == 1
    assert jeff["fumble_lost"] == 1

    ray = next(p for p in normalized if p["player_id"] == 990)
    assert ray["total_fumbles"] == 1
    assert ray["fumble_lost"] == 0
    assert ray["fumble_recovery"] == 1

    print("Passed all fumble normalizer tests!")

if __name__ == "__main__":
    test_fumble_normalizer()