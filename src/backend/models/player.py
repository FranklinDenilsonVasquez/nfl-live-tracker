from pydantic import BaseModel

# Base player class
class Player(BaseModel):
    playerId: int
    playerName: str
    position: str
    img: str
    jerseyNumber: int
    season: str

