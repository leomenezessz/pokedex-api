from pydantic import BaseModel, ConfigDict


class Sprite(BaseModel):
    model_config = ConfigDict(extra="ignore")
    front_default: str = None


class Pokemon(BaseModel):
    model_config = ConfigDict(extra="ignore")
    name: str
    sprites: Sprite



