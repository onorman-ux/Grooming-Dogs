from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict


class PetBase(BaseModel):
    customer_id: int
    name: str
    breed: Optional[str] = None
    weight: Optional[Decimal] = None
    notes: Optional[str] = None


class PetCreate(PetBase):
    pass


class PetUpdate(BaseModel):
    customer_id: Optional[int] = None
    name: Optional[str] = None
    breed: Optional[str] = None
    weight: Optional[Decimal] = None
    notes: Optional[str] = None


class Pet(PetBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
