from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.user_model import User
from schemas.user_schema import UserOut

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/all", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


