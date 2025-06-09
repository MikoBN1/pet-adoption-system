from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import and_
from core.security import get_current_user
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.favorite_pets_model import FavoritePets
from models.user_model import User
from schemas.favorite_pets_schema import FavoritePets as FavoritePetsSchema, FavoritePetsCreate

router = APIRouter(prefix="/favorites", tags=["favorites"])

@router.get("/all", response_model=List[FavoritePetsSchema])
async def get_favorites(db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user)):
    result = await db.execute(select(FavoritePets).where(FavoritePets.user_id == user.id))
    favorites = result.scalars().all()
    return favorites

@router.get("/{pet_id}", response_model=FavoritePetsSchema)
async def get_favorite_pet(pet_id:int, db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user)):
    print(user)
    result = await db.execute(select(FavoritePets).where(and_(FavoritePets.pet_id == pet_id, FavoritePets.user_id == user.id)))
    favorite_pet = result.scalars().first()
    if not favorite_pet:
        raise HTTPException(status_code=404, detail="Favorite pet not found")
    return favorite_pet

@router.post("/new", response_model=FavoritePetsSchema)
async def create_favorite_pet(data: FavoritePetsCreate, db:AsyncSession = Depends(get_db), user: User = Depends(get_current_user)):
    new_favorite = FavoritePets(pet_id = data.pet_id, user_id = user.id)
    db.add(new_favorite)
    await db.commit()
    await db.refresh(new_favorite)
    return new_favorite

@router.delete("/{pet_id}", response_model=dict[str, str])
async def delete_favorite_pet(pet_id: int, db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user)):
    result = await db.execute(select(FavoritePets).where(and_(FavoritePets.pet_id == pet_id, FavoritePets.user_id == user.id)))
    favorite_pet = result.scalars().first()

    if not favorite_pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    await db.delete(favorite_pet)
    await db.commit()

    return {"message": "Deleted successfully"}