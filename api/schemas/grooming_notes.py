from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class GroomingNoteBase(BaseModel):
    appointment_id: int
    pet_id: int
    groomer_id: int
    note_text: str


class GroomingNoteCreate(GroomingNoteBase):
    pass


class GroomingNoteUpdate(BaseModel):
    appointment_id: Optional[int] = None
    pet_id: Optional[int] = None
    groomer_id: Optional[int] = None
    note_text: Optional[str] = None


class GroomingNote(GroomingNoteBase):
    id: int
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
