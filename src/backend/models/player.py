from pydantic import BaseModel

# Base player class
class Player(BaseModel):
    playerId: int
    playerName: str
    position: str
    img: str
    jerseyNumber: int
    season: str

# p.player_id, p.player_name, p.position_id, p.player_img, pt.jersey_number
