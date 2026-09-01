from psycopg2.extras import execute_values
from psycopg2 import DatabaseError, IntegrityError
from src.backend.utils.logging import logger

# Player Game Rating is a derived cache (see docs/adr/0001), so unlike the raw
# per-game stat tables this upserts on conflict instead of doing nothing -
# a recomputed rating should overwrite the previously stored one.
def upsert_player_game_ratings(cursor, rating_values):
    if not rating_values:
        return

    query = """
        INSERT INTO player_game_rating (player_id, game_id, rating)
        VALUES %s
        ON CONFLICT (player_id, game_id) DO UPDATE
        SET rating = EXCLUDED.rating
    """

    try:
        execute_values(cursor, query, rating_values)
    except IntegrityError as e:
        logger.warning(f"Duplicate entry detected or constraint violation: {e}")
    except DatabaseError as e:
        logger.error(f"Database error occurred: {e}")
        raise
