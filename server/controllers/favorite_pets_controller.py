from typing import List
from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.favorite_pets_model import FavoritePets
from schemas.favorite_pets_schema import FavoritePets as FavoritePetsSchema, FavoritePetsCreate

router = APIRouter(prefix="/favorites", tags=["favorites"])

@router.get("/all", response_model=List[FavoritePetsSchema])
async def get_favorites(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(FavoritePets))
    favorites = result.scalars().all()
    return favorites

@router.get("/{pet_id}", response_model=FavoritePetsSchema)
async def get_favorite_pet(pet_id:int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(FavoritePets).where(FavoritePets.pet_id == pet_id))
    favorite_pet = result.scalars().first()
    return favorite_pet

@router.post("/new", response_model=FavoritePetsSchema)
async def create_favorite_pet(data: FavoritePetsCreate, db:AsyncSession = Depends(get_db)):
    new_favorite = FavoritePets(**data.dict())
    db.add(new_favorite)
    await db.commit()
    await db.refresh(new_favorite)
    return new_favorite