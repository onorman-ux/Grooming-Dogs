from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATE, TIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
    groomer_id = Column(Integer, ForeignKey("groomers.id"), nullable=False)
    service_id = Column(Integer, ForeignKey("grooming_services.id"), nullable=False)
    appointment_date = Column(DATE, nullable=False)
    start_time = Column(TIME, nullable=False)
    total_price = Column(DECIMAL(10, 2), nullable=False)
    status = Column(String(50), nullable=False)

    customer = relationship("Customer", back_populates="appointments")
    pet = relationship("Pet", back_populates="appointments")
    groomer = relationship("Groomer", back_populates="appointments")
    grooming_service = relationship("GroomingService", back_populates="appointments")
    payment = relationship("Payment", back_populates="appointment", uselist=False)
    review = relationship("Review", back_populates="appointment", uselist=False)
    grooming_notes = relationship("GroomingNote", back_populates="appointment")
