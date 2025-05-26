from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password_hash = Column(Text)
    phone = Column(String)
    role = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    # pets = relationship("Pet", back_populates="shelter")
    # favorites = relationship("Favorite", back_populates="user")