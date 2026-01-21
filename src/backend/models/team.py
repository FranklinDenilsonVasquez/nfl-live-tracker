from pydantic import BaseModel
from src.backend.models.stadium import Stadium

# Base team class
class Team(BaseModel):
    teamId: int
    teamName: str
    stadium: Stadium
    city: str
    code: str
    logo: str
