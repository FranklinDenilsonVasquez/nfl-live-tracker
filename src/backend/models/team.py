from pydantic import BaseModel
from src.backend.models.stadium import Stadium

# Base team class
class Team(BaseModel):
    team_id: int
    team_name: str
    stadium: Stadium
    city: str
    code: str
    logo: str
