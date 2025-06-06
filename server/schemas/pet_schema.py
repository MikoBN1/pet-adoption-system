from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class PetBase(BaseModel):
    name: Optional[str] = None
    species: Optional[str] = None
    breed: Optional[str] = None
    age: Optional[int] = None
    description: Optional[str] = None
    is_adopted: Optional[bool] = None
    shelter_id: Optional[int] = None
    image_url: Optional[str] = None

class PetCreate(BaseModel):
    name: str
    species: str
    breed: str
    age: int
    description: str
    is_adopted: bool
    shelter_id: int
    image_url: str

class Pet(PetBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
