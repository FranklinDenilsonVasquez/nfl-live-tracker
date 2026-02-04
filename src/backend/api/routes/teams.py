from fastapi import APIRouter, HTTPException, Query
from src.backend.db.queries import get_all_teams
from src.backend.models.team import Team
from src.backend.models.stadium import Stadium


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