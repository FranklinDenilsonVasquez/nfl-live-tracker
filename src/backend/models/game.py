from pydantic import BaseModel
from datetime import date
from src.backend.models.team import Team
from src.backend.models.season import Season

class Game (BaseModel):
    gameId: int
    homeTeam: Team
    awayTeam: Team
    date: date
    homeTeamScore: int
    awayTeamScore: int
    season: Season
    status: str
    stage: str
    week: str
    venue: str
    city: str
