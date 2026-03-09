from pydantic import BaseModel

# Base player class
class Player(BaseModel):
    player_id: int
    player_name: str
    position: str
    img: str
    jersey_number: int
    season: str
    height: str | None = None
    weight: str | None = None
    college: str | None = None
    team: str | None = None
