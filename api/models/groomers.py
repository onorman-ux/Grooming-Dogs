from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Groomer(Base):
    __tablename__ = "groomers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    specialty = Column(String(100))

    appointments = relationship("Appointment", back_populates="groomer")
    schedules = relationship("Schedule", back_populates="groomer")
    reviews = relationship("Review", back_populates="groomer")
    grooming_notes = relationship("GroomingNote", back_populates="groomer")
