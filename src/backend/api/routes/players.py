from fastapi import APIRouter, HTTPException, Query
from src.backend.services.player_service import fetch_player
from src.backend.models.player import Player

router = APIRouter(prefix="/players", tags=["Players"])

# Search player by name
@router.get("/search", response_model=list[Player])
def search_players(name: str = Query(...,
                                     description="Player name or partial name"),
                   season: int = Query(..., description="Season year"),
                   team_id: int | None = Query(None, description="Optional team filter")
                   ):
    from src.backend.services.player_service import search_player_by_name

    players = search_player_by_name(name, season, team_id)

    if not players:
        raise HTTPException(
            status_code=404,
            detail="No players found"
        )
    return players

# Search player by player_id and season
@router.get("/{player_id}", response_model=Player)
def get_player(player_id: int, season: int):
    player = fetch_player(player_id, season)

    if not player:
        raise HTTPException(
            status_code=404,
            detail="No player found"
        )
    return player

# Search players by name for a given season. Can also filter by team.
