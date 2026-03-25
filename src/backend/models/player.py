from pydantic import BaseModel
from src.backend.models.season import Season

# Base player class
class Player(BaseModel):
    player_id: int
    player_name: str
    position: str
    player_img: str
    jersey_number: int
    season_id: int
    height: str | None = None
    weight: str | None = None
    college: str | None = None
    team: str | None = None
