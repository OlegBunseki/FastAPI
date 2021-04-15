from pydantic import BaseModel


class UmbrellaStatus(BaseModel):
    weather_category: str
    bring_umbrella: bool
    temp: float
