from sqlalchemy import Column, Integer, String, Float
from database.base import Base

class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    country = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(500))