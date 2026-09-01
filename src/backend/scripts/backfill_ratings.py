# One-off, idempotent backfill of Player Game Rating (see CONTEXT.md,
# docs/adr/0001-absolute-baseline-player-game-rating.md) for games whose
# stats were already ingested before this feature existed.
# Run with: python -m src.backend.scripts.backfill_ratings
from psycopg2.extras import RealDictCursor
from src.backend.database.db_connection import get_db_connection
from src.backend.database.repositories.player_repository import get_player_position_map
from src.backend.database.inserts.rating import upsert_player_game_ratings
from src.backend.core.player_rating import compute_game_rating
from src.backend.utils.logging import setup_logger

logger = setup_logger()

# Only the tables backing positions in the v1 rating scope; KR/PR/G/OT are
# deliberately excluded (see docs/adr/0001).
STAT_TABLES = [
    "player_passing_stats",
    "player_rushing_stats",
    "player_receiving_stats",
    "player_fumble_stats",
    "player_defense_stats",
    "player_interception_stats",
    "player_kicking_stats",
    "player_punting_stats",
]


def _fetch_all_stats(cursor):
    merged = {}

    for table in STAT_TABLES:
        cursor.execute(f"SELECT * FROM {table};")
        for row in cursor.fetchall():
            key = (row["player_id"], row["game_id"])
            merged.setdefault(key, {}).update(row)

    return merged


def backfill_ratings():
    conn = get_db_connection()
    if not conn:
        raise Exception("Failed to connect to database")

    try:
        with conn.cursor(cursor_factory=RealDictCursor) as dict_cursor:
            merged_stats = _fetch_all_stats(dict_cursor)
        logger.info(f"Loaded stat lines for {len(merged_stats)} (player, game) pairs.")

        # get_player_position_map/upsert_player_game_ratings expect plain
        # (non-dict) rows, so use a separate cursor from the RealDictCursor
        # above (which _fetch_all_stats needs for column-name access).
        with conn.cursor() as cursor:
            player_ids = {player_id for (player_id, _game_id) in merged_stats}
            position_map = get_player_position_map(cursor, player_ids)

            rating_values = []
            for (player_id, game_id), stats in merged_stats.items():
                position = position_map.get(player_id)
                if not position:
                    continue

                rating = compute_game_rating(position, stats)
                if rating is None:
                    continue

                rating_values.append((player_id, game_id, rating))

            logger.info(f"Computed {len(rating_values)} ratings, upserting.")
            upsert_player_game_ratings(cursor, rating_values)

        conn.commit()
        logger.info("Rating backfill complete.")
    except Exception:
        conn.rollback()
        logger.exception("Rating backfill failed")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    backfill_ratings()
