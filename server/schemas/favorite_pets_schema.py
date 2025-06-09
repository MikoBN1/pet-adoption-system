from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FavoritePetsBase(BaseModel):
    user_id: Optional[int] = None
    pet_id: Optional[int] = None

class FavoritePetsCreate(FavoritePetsBase):
    pet_id: int

class FavoritePets(FavoritePetsBase):
    id: int
    added_at: datetime

    class Config:
        orm_mode = True
