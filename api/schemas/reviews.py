from typing import Optional
from pydantic import BaseModel, ConfigDict


class ReviewBase(BaseModel):
    appointment_id: int
    customer_id: int
    groomer_id: int
    rating: int
    review_text: Optional[str] = None


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    appointment_id: Optional[int] = None
    customer_id: Optional[int] = None
    groomer_id: Optional[int] = None
    rating: Optional[int] = None
    review_text: Optional[str] = None


class Review(ReviewBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
