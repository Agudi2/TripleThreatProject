from typing import Optional
from pydantic import BaseModel

class FeedbackBase(BaseModel):
    customer_name: str
    rating: int
    comments: Optional[str] = None

class FeedbackCreate(FeedbackBase):
    pass

class FeedbackUpdate(BaseModel):
    customer_name: Optional[str] = None
    rating: Optional[int] = None
    comments: Optional[str] = None

class Feedback(FeedbackBase):
    id: int

    class Config:
        orm_mode = True
