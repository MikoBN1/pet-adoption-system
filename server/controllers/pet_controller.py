from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.pet_model import Pet
from schemas.pet_schema import PetBase, PetCreate

router = APIRouter(prefix="/pets", tags=["pets"])

@router.get("/all", response_model=List[PetBase])
def get_pets(db: Session = Depends(get_db)):
    pets = db.query(Pet).all()
    return pets

@router.get("/{pet_id}")
def get_user(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(Pet).filter(Pet.id == pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="User not found")
    return pet

@router.post("/new", response_model=PetBase)
def create_pet(pet_data: PetCreate, db: Session = Depends(get_db)):
    new_pet = Pet(**pet_data.dict())
    db.add(new_pet)
    db.commit()
    db.refresh(new_pet)
    return new_pet




