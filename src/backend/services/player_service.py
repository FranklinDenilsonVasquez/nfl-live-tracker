from src.backend.core.position_model_mapping import POSITION_MODEL_MAP_PER_SEASON
from src.backend.database.queries.player_queries import get_all_player_games_stats
from src.backend.database.db_connection import get_db_connection
from src.backend.database.queries.player_queries import (get_player_by_id, get_player_by_name,
                                                         get_player_stats, get_all_player_games_stats)
from src.backend.models.player import Player
from src.backend.models.player_stats import (QBStats, SkillStats, DefenseStats, KickerStats, PunterStats,
                                             KickReturnerStats, PuntReturnerStats)
from pprint import pprint
from src.backend.utils.logging import logger


# Service for fetching player by player_id and season
def fetch_player(player_id: int, season: int):
    conn = get_db_connection()
    if not conn:
        raise Exception("Failed to connect to database")
    try:
        with conn.cursor() as cursor:
            player_row = get_player_by_id(cursor, player_id, season)
            if not player_row:
                return None
            return Player(
                player_id=player_id,
                player_name=player_row[0],
                position=player_row[1],
                player_img=player_row[2],
                jersey_number=player_row[3],
                season_id=season,
                height=player_row[4],
                weight=player_row[5],
                college=player_row[6],
                team=player_row[7]
            )
    finally:
        conn.close()

# Service for fetching player by name
def search_player_by_name(name: str, season: int, team_id: int | None):
    conn = get_db_connection()
    if not conn:
        raise Exception("Failed to connect to database")
    try:
        with conn.cursor() as cursor:
            player_row = get_player_by_name(cursor, name, season, team_id)
            if not player_row:
                return None
            return [
                Player(
                    player_name=row[0],
                    position=row[1],
                    player_img=row[2],
                    jersey_number=row[3],
                    season=str(season),
                    height=row[4],
                    weight=row[5],
                    college=row[6],
                    team=row[7],
                    player_id=row[8]
                )
                for row in player_row
            ]
    finally:
        conn.close()


# Service for fetching player stats (filter by specific season)
def get_player_season_stats(player_id: int, season: int | None):
    conn = get_db_connection()
    if not conn:
        raise Exception("Failed to connect to database")
    try:
        with conn.cursor() as cursor:
            player_stat_row = get_player_stats(cursor, player_id, season)

            if not player_stat_row:
                logger.warning("No player data found")
                return None

            pprint(player_stat_row, sort_dicts=False)

            from src.backend.core.position_model_mapping import POSITION_MODEL_MAP_PER_SEASON
            position = player_stat_row['position']
            if not position:
                logger.warning("Can't find the players position from the data returned")
                return None
            model = POSITION_MODEL_MAP_PER_SEASON.get(position, DefenseStats)

            return model(**player_stat_row)

    finally:
        conn.close()


# Service for fetching all games a certain player has played in along with his stats for each game
def get_player_game_stats(player_id: int, team_id: int | None, season_id: int):
    conn = get_db_connection()
    if not conn:
        raise Exception("Failed to connect to database")
    try:
        with conn.cursor() as cursor:
            player_stats = get_all_player_games_stats(cursor, player_id, team_id, season_id)

            if not player_stats:
                logger.warning("No player data found.")
                return None
        pprint(player_stats, sort_dicts=False)

        position = player_stats.get('position')
        if not position:
            logger.warning("Can't find the players position from the data returned")
            return None

        from src.backend.core.position_model_mapping import POSITION_MODEL_MAP_PER_GAME
        model = POSITION_MODEL_MAP_PER_GAME.get(position, DefenseStats)
        if not model:
            logger.warning(f"Can't map correct model: "
                           f"position : {position} "
                           f"model: {model}")

        from src.backend.models.game import PlayerGamesResponse
        return model(**player_stats)
    finally:
        conn.close()
