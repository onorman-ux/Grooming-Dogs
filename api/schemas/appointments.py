from datetime import date, time
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict


class AppointmentBase(BaseModel):
    customer_id: int
    pet_id: int
    groomer_id: int
    service_id: int
    appointment_date: date
    start_time: time
    total_price: Decimal
    status: str


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentUpdate(BaseModel):
    customer_id: Optional[int] = None
    pet_id: Optional[int] = None
    groomer_id: Optional[int] = None
    service_id: Optional[int] = None
    appointment_date: Optional[date] = None
    start_time: Optional[time] = None
    total_price: Optional[Decimal] = None
    status: Optional[str] = None


class Appointment(AppointmentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
