from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=False, unique=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    groomer_id = Column(Integer, ForeignKey("groomers.id"), nullable=False)
    rating = Column(Integer, nullable=False)
    review_text = Column(String(500))

    appointment = relationship("Appointment", back_populates="review")
    customer = relationship("Customer", back_populates="reviews")
    groomer = relationship("Groomer", back_populates="reviews")
