from fastapi import APIRouter, HTTPException
from src.backend.models.standings import StandingResponseWrapper
from src.backend.services.standing_service import get_season_standings

router = APIRouter(prefix="/standing", tags=["Standing"])

@router.get("/{season_id}", response_model=StandingResponseWrapper)
def get_standings(season_id: int): 
    standings = get_season_standings(season_id)

    if not standings:
        raise HTTPException(
            status_code=404,
            detail="No standings data found"
        )
    
    return standings