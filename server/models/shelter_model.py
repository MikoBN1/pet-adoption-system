from sqlalchemy import Column, Integer, String

from database import Base

class ShelterProfile(Base):
    __tablename__ = "shelter_profiles"

    shelter_id = Column(Integer, primary_key=True, index=True)
    shelter_name = Column(String)
    address = Column(String)
    description = Column(String)
    website = Column(String)
