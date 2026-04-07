from pydantic import BaseModel, Field

from ..enum import CategoryEnum


class BatchResponse(BaseModel):
    command: int
    category: CategoryEnum
    