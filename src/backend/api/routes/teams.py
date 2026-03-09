from fastapi import APIRouter, HTTPException, Query
from src.backend.database.queries.queries import get_all_teams, get_players_by_team
from src.backend.models.team import Team
from src.backend.models.stadium import Stadium
from src.backend.models.player import Player


router = APIRouter(prefix="/teams", tags=["Teams"])

@router.get("/", response_model=list[Team])
def get_teams():
    teams = get_all_teams()

    if not teams:
        raise HTTPException(
            status_code=404,
            detail="No teams found"
        )

    return [
        Team(
            team_id=row[0],
            team_name=row[1],
            city=row[2],
            code=row[3],
            logo=row[4],
            stadium=Stadium(
                stadium_id=row[5],
                name=row[6],
                location=row[7],
                capacity=row[8]
            ),

    ) for row in teams
    ]

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