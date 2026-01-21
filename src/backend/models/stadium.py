from pydantic import BaseModel

class Stadium (BaseModel):
    stadiumId: int
    name: str
    capacity: int
    location: str