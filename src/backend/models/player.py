from pydantic import BaseModel

# Base player class
class Player(BaseModel):
    playerId: int
    teamId: int
    positionId: int
    positionType: str
    fullName: str
    rosterStatus: str
    seasonYear: int


