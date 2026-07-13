from sqlalchemy import Column, ForeignKey, Integer, String, DATE, TIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    groomer_id = Column(Integer, ForeignKey("groomers.id"), nullable=False)
    schedule_date = Column(DATE, nullable=False)
    start_time = Column(TIME, nullable=False)
    end_time = Column(TIME, nullable=False)
    status = Column(String(50), nullable=False)

    groomer = relationship("Groomer", back_populates="schedules")
