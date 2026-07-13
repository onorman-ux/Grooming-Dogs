from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict


class GroomingServiceBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    duration: int


class GroomingServiceCreate(GroomingServiceBase):
    pass


class GroomingServiceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    duration: Optional[int] = None


class GroomingService(GroomingServiceBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
