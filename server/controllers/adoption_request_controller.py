from typing import List
from fastapi import APIRouter, Depends
from database import get_db
from models.adoption_request_model import AdoptionRequest
from schemas.adoption_request_schema import AdoptionRequest as AdoptionRequestSchema
from schemas.adoption_request_schema import AdoptionRequestCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
router = APIRouter(prefix="/adoption", tags=["adoption"])

@router.get("/all", response_model=List[AdoptionRequestSchema])
async def get_all_adoptions(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(AdoptionRequest))
    adoption_requests = result.scalars().all()
    return adoption_requests

@router.post("/new", response_model=AdoptionRequestCreate)
async def create_adoption_request(data: AdoptionRequestCreate, db: AsyncSession = Depends(get_db)):
    new_adoption_request = AdoptionRequest(**data.dict())
    db.add(new_adoption_request)
    await db.commit()
    await db.refresh(new_adoption_request)
    return new_adoption_request
