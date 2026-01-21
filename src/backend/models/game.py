from pydantic import BaseModel
from datetime import date
from src.backend.models.team import Team
from src.backend.models.season import Season

class Game (BaseModel):
    game_id: int
    home_team: Team
    away_team: Team
    date: date
    home_team_score: int
    away_team_score: int
    season: Season
    status: str
    stage: str
    week: str
    venue: str
    city: str
