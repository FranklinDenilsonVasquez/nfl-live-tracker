from fastapi import APIRouter, HTTPException, Query
from typing import List
from src.backend.services.game_service import get_games_list
from src.backend.models.game import Game

router = APIRouter(prefix="/games", tags=["Games"])

def row_to_dict(row):
    """
    Recursively convert RealDictRow and nested dicts to plain Python dicts.
    """
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