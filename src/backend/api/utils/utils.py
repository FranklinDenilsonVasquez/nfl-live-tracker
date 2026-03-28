from src.backend.utils.logging import logger
from src.backend.database.db_connection import get_db_connection


# Utils used in API development

def get_season_year(cursor, season_id : int):
    try:
        with cursor:
            query = """
                SELECT s.season_id 
                FROM season s 
                WHERE s.season_year = %s
            """

            cursor.execute(query, (season_id, ))
            data = cursor.fetchone()

            if not data:
                logger.warning(f"No season_year exists with season_id: {season_id}")
                return None
            return data[0]
    except Exception as e:
        raise Exception(f"Error when running 'get_season_year' function: {e}")


def get_season_id(cursor, season_year: int):
    try:
        query = "SELECT season_id FROM season WHERE season_year = %s"
        cursor.execute(query, (season_year,))
        data = cursor.fetchone()

        if not data:
            logger.warning(f"No season_id found for season_year: {season_year}")
            return None

        return data[0]
    except Exception as e:
        logger.error(f"Error fetching season_id for year {season_year}: {e}")
        return None