from pydantic import BaseModel
from typing import Optional
from src.backend.models.team import TeamSummary

class Standing (BaseModel):
    id: int
    season_id: int
    team_id: int
    conference: str
    division: str
    position: int
    wins: int
    losses: int
    ties: int
    points_for: int
    points_against: int
    point_differential: int
    conference_wins: int
    conference_losses: int
    division_wins: int
    division_losses: int
    home_wins: int 
    home_losses: int
    road_wins: int
    road_losses: int 
    streak: str

class StandingResponse(BaseModel):
    team: TeamSummary
    conference: str
    division: str
    position: int
    wins: int
    losses: int
    ties: int
    points_for: int
    points_against: int
    point_differential: int
    conference_wins: int
    conference_losses: int
    division_wins: int
    division_losses: int
    home_wins: int 
    home_losses: int
    road_wins: int
    road_losses: int 
    streak: str

class StandingResponseWrapper(BaseModel):
    season_year: int
    standings: list[StandingResponse]
