from pydantic import BaseModel

class Stadium (BaseModel):
    stadium_id: int
    name: str
    capacity: int
    location: str