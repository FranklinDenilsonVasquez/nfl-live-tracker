from pydantic import BaseModel

class Season (BaseModel):
    seasonId: int
    seasonYear: str