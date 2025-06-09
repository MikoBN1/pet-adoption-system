from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.security import get_current_user, require_admin
from database import get_db
from models.user_model import User
from schemas.user_schema import UserOut

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/all", response_model=List[UserOut])
async def get_users(db: AsyncSession = Depends(get_db), admin_user: User = Depends(require_admin)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users

@router.get("/me", response_model=UserOut)
async def read_profile(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/admin-area")
async def admin_only_area(admin_user: User = Depends(require_admin)):
    return {"msg": f"Hello, admin {admin_user.name}"}

@router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db), admin_user: User = Depends(require_admin)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
