from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.pet_model import Pet
from schemas.pet_schema import Pet as PetResponse
from schemas.pet_schema import PetBase, PetCreate

router = APIRouter(prefix="/pets", tags=["pets"])

@router.get("/all", response_model=List[PetResponse])
def get_pets(db: Session = Depends(get_db)):
    pets = db.query(Pet).all()
    return pets

@router.get("/{pet_id}")
def get_user(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(Pet).filter(Pet.id == pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

@router.post("/new", response_model=PetBase)
def create_pet(pet_data: PetCreate, db: Session = Depends(get_db)):
    new_pet = Pet(**pet_data.dict())
    db.add(new_pet)
    db.commit()
    db.refresh(new_pet)
    return new_pet

@router.patch("/{pet_id}")
def update_pet(pet_id: int, pet_data: PetBase, db: Session = Depends(get_db)):
    update_data = pet_data.dict(exclude_unset=True)

    result = db.query(Pet).filter(Pet.id == pet_id).update(update_data)
    if result == 0:
        raise HTTPException(status_code=404, detail="Pet not found")

    db.commit()
    updated_pet = db.query(Pet).filter(Pet.id == pet_id).first()
    return updated_pet

@router.delete("/{pet_id}")
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(Pet).filter(Pet.id == pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    db.delete(pet)
    db.commit()
    return {"message": "Pet deleted"}




