from sqlalchemy import Column, Integer, String
from ..dependencies.database import Base

class GuestOrder(Base):
    __tablename__ = "guest_orders"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    address = Column(String(255), nullable=False)
    order_description = Column(String(500), nullable=False)
