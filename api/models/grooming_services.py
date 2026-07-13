from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class GroomingService(Base):
    __tablename__ = "grooming_services"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(300))
    price = Column(DECIMAL(10, 2), nullable=False)
    duration = Column(Integer, nullable=False)

    appointments = relationship("Appointment", back_populates="grooming_service")
