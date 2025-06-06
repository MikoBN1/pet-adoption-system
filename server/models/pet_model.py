from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from datetime import datetime

from database import Base

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    species = Column(String)
    breed = Column(Text)
    age = Column(Integer)
    gender = Column(String)
    description = Column(String)
    is_adopted = Column(Boolean)
    shelter_id = Column(Integer, ForeignKey('shelter_profiles.shelter_id'))
    image_url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
