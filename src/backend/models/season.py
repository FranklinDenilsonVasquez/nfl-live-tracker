from pydantic import BaseModel

class Season (BaseModel):
    season_id: int
    season_year: str