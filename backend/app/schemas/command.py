from pydantic import BaseModel


class CommandResponse(BaseModel):
    model_config = {'from_attributes': True}

    id: int
    number: int
    name: str
    full_name: str