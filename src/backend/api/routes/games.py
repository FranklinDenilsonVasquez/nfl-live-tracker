from fastapi import APIRouter, HTTPException, Query
from typing import List
from src.backend.services.game_service import get_games_list, get_game_player_stats
from src.backend.models.game import Game, GamePlayerStatsResponse
from pprint import pprint

router = APIRouter(prefix="/games", tags=["Games"])

# Recursively convert RealDictRow and nested dicts to plain Python dicts.
def row_to_dict(row):
    if hasattr(row, "_asdict"):
        return {k: row_to_dict(v) for k, v in row._asdict().items()}
    elif isinstance(row, dict):
        return {k: row_to_dict(v) for k, v in row.items()}
    elif isinstance(row, list):
        return [row_to_dict(v) for v in row]
    return row

@router.get("/game_list", response_model=List[Game])
def get_games(week: str, season: int, stage: str):
    games = get_games_list(week, season, stage)

    if not games:
        raise HTTPException(
            status_code=404,
            detail="No games found"
        )
    game_dicts = [row_to_dict(game) for game in games]
    return game_dicts

from src.backend.api.utils.stats_cleaner import apply_stat_cleanup
@router.get("/{game_id}/player-stats", response_model=GamePlayerStatsResponse, response_model_exclude_none=True)
def get_game_team_player_stats(game_id: int):
    player_game_stats = get_game_player_stats(game_id)

    if not player_game_stats:
        raise HTTPException(
            status_code=404,
            detail="No player stats found for game."
        )

    stats = apply_stat_cleanup(player_game_stats)

    return stats
