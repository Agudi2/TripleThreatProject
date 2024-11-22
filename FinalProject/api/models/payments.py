from sqlalchemy import Column, Integer, String, Enum
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    card_info = Column(String(100), nullable=False)  # Mask sensitive data in production
    transaction_status = Column(String(50), nullable=False)  # E.g., 'Success', 'Pending', 'Failed'
    payment_type = Column(Enum("Credit", "Debit", "Cash", "Online", name="payment_type"), nullable=False)