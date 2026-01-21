from pydantic import BaseModel

# Base player class
class Player(BaseModel):
    player_id: int
    player_name: str
    position: str
    img: str
    jersey_number: int
    season: str

