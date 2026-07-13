from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class GroomingNote(Base):
    __tablename__ = "grooming_notes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=False)
    pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
    groomer_id = Column(Integer, ForeignKey("groomers.id"), nullable=False)
    note_text = Column(String(500), nullable=False)
    created_at = Column(DATETIME, nullable=False, server_default=str(datetime.now()))

    appointment = relationship("Appointment", back_populates="grooming_notes")
    pet = relationship("Pet", back_populates="grooming_notes")
    groomer = relationship("Groomer", back_populates="grooming_notes")
