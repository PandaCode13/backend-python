from sqlalchemy import Column, Integer, Date, ForeignKey
from database.base import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    destination_id = Column(Integer, ForeignKey("destinations.id"), nullable=False)
    travel_date = Column(Date, nullable=False)
    number_of_people = Column(Integer, nullable=False)