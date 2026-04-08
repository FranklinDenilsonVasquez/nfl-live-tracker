from fastapi import APIRouter, HTTPException, Query
from typing import List
from src.backend.services.game_service import get_games_list
from src.backend.models.game import Game

router = APIRouter(prefix="/games", tags=["Games"])

@router.get("/game_list", response_model=List[Game])
def get_games(week: str, season: int, stage: str):
    games = get_games_list(week, season, stage)

    if not games:
        raise HTTPException(
            status_code=404,
            detail="No games found"
        )

    return games