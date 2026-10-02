from pydantic import BaseModel, ValidationError


class HorizonResponse(BaseModel):
    signature: dict
    result: str
