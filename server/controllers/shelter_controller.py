from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.shelter_model import ShelterProfile
from schemas.shelter_schema import ShelterBase

router = APIRouter(prefix="/shelters", tags=["shelters"])

@router.get("/all", response_model=List[ShelterBase])
def get_shelters(db: Session = Depends(get_db)):
    shelters = db.query(ShelterProfile).all()
    return shelters



