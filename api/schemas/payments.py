from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict


class PaymentBase(BaseModel):
    appointment_id: int
    customer_id: int
    amount: Decimal
    payment_method: str
    payment_status: str


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    appointment_id: Optional[int] = None
    customer_id: Optional[int] = None
    amount: Optional[Decimal] = None
    payment_method: Optional[str] = None
    payment_status: Optional[str] = None


class Payment(PaymentBase):
    id: int
    payment_date: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
