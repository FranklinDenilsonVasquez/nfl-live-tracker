from fastapi import APIRouter, HTTPException, Query
from typing import Union
from src.backend.services import player_service
from src.backend.models.player import Player
from src.backend.models.player_stats import (QBStats, QBStatsPerGame, SkillStats, DefenseStats, KickerStats, PunterStats,
                                             KickReturnerStats, PuntReturnerStats, LinemenStats)
from src.backend.models.game import PlayerGamesResponse

router = APIRouter(prefix="/players", tags=["Players"])

# Search players by name for a given season. Can also filter by team.
@router.get("/search", response_model=list[Player])
def search_players(name: str = Query(...,
                                     description="Player name or partial name"),
                   season: int = Query(..., description="Season year"),
                   team_id: int | None = Query(None, description="Optional team filter")
                   ):

    players = player_service.search_player_by_name(name, season, team_id)

    if not players:
        raise HTTPException(
            status_code=404,
            detail="No players found"
        )
    return players

# Search player by player_id and season
@router.get("/{player_id}", response_model=Player)
def get_player(player_id: int, season: int):
    player = player_service.fetch_player(player_id, season)

    if not player:
        raise HTTPException(
            status_code=404,
            detail="No player found"
        )
    return player

# Search player season stats with player_id
@router.get("/{player_id}/stats", response_model=Union[QBStats, SkillStats, DefenseStats, KickerStats, PunterStats,
                                             KickReturnerStats, PuntReturnerStats, LinemenStats])
def get_player_season_stats(player_id: int, season: int = Query(None)):
    player_stats = player_service.get_player_season_stats(player_id, season)

    if not player_stats:
        raise HTTPException(
            status_code=404,
            detail="No player found"
        )
    return player_stats


# Return a list of games the player played in, with stats for that player
@router.get("/{player_id}/games", response_model=PlayerGamesResponse)
def get_player_game_stats(player_id: int, season: int, team_id: int | None = Query(None,)):
    player_stats = player_service.get_player_game_stats(player_id, season, team_id)

    if not player_stats:
        raise HTTPException(
            status_code=404,
            detail="No player found"
        )
    return player_stats



# Filter players by position


# Player leaders for each stat group


# Optional: player career stats