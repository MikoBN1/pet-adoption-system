from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.user_model import User
from schemas.user_schema import User as UserSchema
router = APIRouter(prefix="/user", tags=["user"])

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    print(user.name)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

