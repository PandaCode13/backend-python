from sqlalchemy import Column, Integer, Float, String, ForeignKey
from database.base import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"), nullable=False)
    amount = Column(Float, nullable=False)
    payment_method = Column(String(50), nullable=False)
    status = Column(String(30), default="pending")