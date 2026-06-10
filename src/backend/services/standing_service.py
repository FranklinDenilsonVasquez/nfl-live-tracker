from src.backend.utils.logging import logger
from pprint import pprint
from src.backend.database.db_connection import get_db_connection
from src.backend.database.queries.standing_queries import get_standings
from src.backend.api.utils.utils import get_season_id
from src.backend.models.standings import StandingResponse, StandingResponseWrapper
from src.backend.models.team import TeamSummary

def get_season_standings(season_year: int):
    conn = get_db_connection()
    

    if not conn: 
        raise Exception("Failed to connect to database")
    
    try:
        cursor = conn.cursor()
        season_id = get_season_id(cursor, season_year)
        # print(f"HHHHHHHHHH {season_id}")
        rows = get_standings(cursor, season_id)

        if not season_year or not rows:
            logger.warning(f"Error getting standing details for year : {season_year}")
            return None

        # print(f"Season: {season_year}")
        # print(f"Standings: {standings}")

        standings = []

        for row in rows:
            standings.append(
                StandingResponse(
                    team=TeamSummary(
                        team_id=row["team_id"],
                        team_name=row["team_name"],
                        logo=row["logo_path"]
                    ),
                    conference=row["conference"],
                    division=row["division"],
                    position=row["position"],
                    wins=row["wins"],
                    losses=row["losses"],
                    ties=row["ties"],
                    points_for=row["points_for"],
                    points_against=row["points_against"],
                    point_differential=row["point_differential"],
                    conference_wins=row["conference_wins"],
                    conference_losses=row["conference_losses"],
                    division_wins=row["division_wins"],
                    division_losses=row["division_losses"],
                    home_wins=row["home_wins"],
                    home_losses=row["home_losses"],
                    road_wins=row["road_wins"],
                    road_losses=row["road_losses"],
                    streak=row["streak"]
                )
            )

        return StandingResponseWrapper(
            season_year=season_year,
            standings=standings
        )
    
    finally:
        cursor.close()
        conn.close()