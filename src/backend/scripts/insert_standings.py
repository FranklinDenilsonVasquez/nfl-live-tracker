from src.backend.api.fetch_data import fetch_standings
from src.backend.database.inserts.standings import insert_standings
from src.backend.database.normalizers.standings import normalize_standing_stats
from src.backend.utils.logging import setup_logger as logger
from src.backend.database.db_connection import get_db_connection
import pprint 
from pprint import pprint

def main():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        if not conn:
            logger.warning("Connection to database failed")
            return
    
        season = 2024
        standings = fetch_standings(1, season)

        if not standings:
            logger.warning(f"Unable to fetch standings for season {season}")
            return 
        
        # print(f"Raw standings: ")
        # pprint(standings)

        normalize_standings = normalize_standing_stats(cursor, standings)

        # print(f"Normalized standings: ")
        # pprint(normalize_standings)

        if normalize_standings:
            insert_standings(cursor, normalize_standings)
            conn.commit()
            print("Standings committed")
    except Exception as e:
        if conn: 
            conn.rollback()

        logger.error(f"ET: failed: {e}")
        raise
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        
    
if __name__ == "__main__":
    main()
