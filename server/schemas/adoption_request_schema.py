from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AdoptionRequestBase(BaseModel):
    adopter_id: Optional[int] = None
    pet_id: Optional[int] = None
    status: Optional[str] = None
    message: Optional[str] = None

class AdoptionRequestCreate(AdoptionRequestBase):
    adopter_id: int
    pet_id: int
    status: str
    message: str

class AdoptionRequest(AdoptionRequestBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
