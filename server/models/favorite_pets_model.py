from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime

from database import Base

class FavoritePets(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    pet_id = Column(Integer, ForeignKey('pets.id'))
    added_at = Column(DateTime, default=datetime.utcnow)
