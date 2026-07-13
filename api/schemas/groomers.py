from typing import Optional
from pydantic import BaseModel, ConfigDict


class GroomerBase(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: str
    specialty: Optional[str] = None


class GroomerCreate(GroomerBase):
    pass


class GroomerUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    specialty: Optional[str] = None


class Groomer(GroomerBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
