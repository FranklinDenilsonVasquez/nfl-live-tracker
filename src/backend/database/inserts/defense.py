from inserts.utils.bulk_insert import bulk_insert
from utils.logging import logger

# Function that takes in a cursor, flat stat list, and the player mapping
# and inserts the defense player stats into PostgreSQL
def insert_defense_player_stat(cursor, stat_list, player_map):
    defense_values = []
    for s in stat_list:
        internal_player_id = player_map.get(s["player_id"])

        if not internal_player_id:
            logger.warning(f"Unknown player_id {s['player_id']}")
            continue

        defense_values.append(
            (internal_player_id,
            s["game_id"],
            s["tackles"],
            s["unassisted_tackles"],
            s["sacks"],
            s["tackles_for_loss"],
            s["passes_defended"],
            s["qb_hits"],
            s["interceptions_for_tds"],
            s["blocked_kicks"],
            s["kick_return_td"],
            s["expected_return_td"],
            s["forced_fumbles"])
        )

    if not defense_values:
        return

    bulk_insert(
        cursor=cursor,
        table_name="player_defense_stats",
        columns=[
            "player_id",
            "game_id",
            "tackles",
            "unassisted_tackles",
            "sacks",
            "tackles_for_loss",
            "passes_defended",
            "qb_hits",
            "interceptions_for_tds",
            "blocked_kicks",
            "kick_return_td",
            "expected_return_td",
            "forced_fumbles"
        ],
        values=defense_values,
        conflict_columns=["player_id", "game_id"]
    )