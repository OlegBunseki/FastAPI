from pydantic import BaseModel
from typing import Optional

class Coordinates(BaseModel):
    x: float
    y: float


class LocationNested(BaseModel):
    city: str
    state: Optional[str] = None
    country: str
    coordinates: Coordinates


class LocationOptional(BaseModel):
    city: str
    state: Optional[str] = None
    country: str
