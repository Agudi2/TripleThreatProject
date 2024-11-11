from sqlalchemy import Column, Integer, String, Text
from ..dependencies.database import Base

class Feedback(Base):
    __tablename__ = "feedbacks"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)
    rating = Column(Integer, nullable=False)  # Assuming rating is an integer value
    comments = Column(Text, nullable=True)   # Optional comments
