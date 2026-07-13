from datetime import date, time
from typing import Optional
from pydantic import BaseModel, ConfigDict


class ScheduleBase(BaseModel):
    groomer_id: int
    schedule_date: date
    start_time: time
    end_time: time
    status: str


class ScheduleCreate(ScheduleBase):
    pass


class ScheduleUpdate(BaseModel):
    groomer_id: Optional[int] = None
    schedule_date: Optional[date] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    status: Optional[str] = None


class Schedule(ScheduleBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
