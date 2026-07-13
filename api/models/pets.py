from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    name = Column(String(100), nullable=False)
    breed = Column(String(100))
    weight = Column(DECIMAL(6, 2))
    notes = Column(String(300))

    customer = relationship("Customer", back_populates="pets")
    appointments = relationship("Appointment", back_populates="pet")
    grooming_notes = relationship("GroomingNote", back_populates="pet")
