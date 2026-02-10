from fastapi import APIRouter, HTTPException, Query
from src.backend.database.queries import get_players_by_team
from src.backend.models.player import Player

router = APIRouter(prefix="/teams", tags=["Players"])

@router.get("/{team_id}/players", response_model=list[Player])
def get_team_players (team_id: int, season: int = Query(..., description="Season year")):
    """
    Get all players for a team in a specific season
    """
    players = get_players_by_team(team_id, season)

    if not players:
        raise HTTPException(
            status_code=404,
            detail=f"No players found for team {team_id} in season {season}"
        )
    return [
        Player(
            player_id=row[0],
            player_name=row[1],
            position=row[2],
            img=row[3],
            jersey_number=row[4],
            season=row[5]
        )
        for row in players
    ]