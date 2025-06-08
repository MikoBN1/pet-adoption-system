from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.security import get_current_user, require_admin
from database import get_db
from models.user_model import User
from schemas.user_schema import UserOut

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/all", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db), admin_user: User = Depends(require_admin)):
    users = db.query(User).all()
    return users

@router.get("/me", response_model=UserOut)
def read_profile(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/admin-area")
def admin_only_area(admin_user: User = Depends(require_admin)):
    return {"msg": f"Hello, admin {admin_user.name}"}

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db), admin_user: User = Depends(require_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
