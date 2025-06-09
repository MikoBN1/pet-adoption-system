from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import get_db
from models.pet_model import Pet
from schemas.pet_schema import Pet as PetResponse
from schemas.pet_schema import PetBase, PetCreate

router = APIRouter(prefix="/pets", tags=["pets"])

@router.get("/all", response_model=List[PetResponse])
async def get_pets(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Pet))
    pets = result.scalars().all()
    return pets

@router.post("/new", response_model=PetBase)
async def create_pet(pet_data: PetCreate, db: AsyncSession = Depends(get_db)):
    new_pet = Pet(**pet_data.dict())
    db.add(new_pet)
    await db.commit()
    await db.refresh(new_pet)
    return new_pet

@router.get("/{pet_id}", response_model=PetResponse)
async def get_pet(pet_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Pet).where(Pet.id == pet_id))
    pet = result.scalars().first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

@router.patch("/{pet_id}", response_model=PetResponse)
async def update_pet(pet_id: int, pet_data: PetBase, db: AsyncSession = Depends(get_db)):
    update_data = pet_data.dict(exclude_unset=True)

    result = await db.execute(select(Pet).where(Pet.id == pet_id))
    pet = result.scalars().first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    for key, value in update_data.items():
        setattr(pet, key, value)

    await db.commit()
    await db.refresh(pet)
    return pet

@router.delete("/{pet_id}")
async def delete_pet(pet_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Pet).where(Pet.id == pet_id))
    pet = result.scalars().first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    await db.delete(pet)
    await db.commit()
    return {"message": "Pet deleted"}
