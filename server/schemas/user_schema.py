from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    role: Optional[str] = None

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str
    phone: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
