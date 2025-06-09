from pydantic import BaseModel
from typing import Optional

class ShelterBase(BaseModel):
    shelter_name: Optional[str] = None
    address: Optional[str] = None
    description: Optional[str] = None
    website: Optional[str] = None

class Shelter(ShelterBase):
    shelter_id: int

    class Config:
        orm_mode = True
