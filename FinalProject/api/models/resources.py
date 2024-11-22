from sqlalchemy import Column, Integer, String, Float
from ..dependencies.database import Base


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)  # Ingredient/resource name
    amount = Column(Float, nullable=False)  # Amount of the resource
    unit = Column(String(50), nullable=False)  # Unit of measurement (e.g., kg, liter, etc.)
