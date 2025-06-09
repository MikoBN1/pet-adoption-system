from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from models.shelter_model import ShelterProfile
from schemas.shelter_schema import ShelterBase

router = APIRouter(prefix="/shelters", tags=["shelters"])

@router.get("/all", response_model=List[ShelterBase])
async def get_shelters(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ShelterProfile))
    shelters = result.scalars().all()
    return shelters



