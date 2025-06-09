from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, String
from datetime import datetime

from database import Base

class AdoptionRequest(Base):
    __tablename__ = "adoption_requests"

    id = Column(Integer, primary_key=True, index=True)
    adopter_id = Column(Integer, ForeignKey('users.id'))
    pet_id = Column(Integer, ForeignKey('pets.id'))
    status = Column(String)
    message = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
