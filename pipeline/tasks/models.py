from pydantic import BaseModel


class HorizonResponse(BaseModel):
    signature: dict
    result: int
