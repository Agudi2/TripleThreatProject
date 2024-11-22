from pydantic import BaseModel
from typing import Literal


class PaymentBase(BaseModel):
    card_info: str  # Consider masking for security in responses
    transaction_status: str  # E.g., 'Success', 'Pending', 'Failed'
    payment_type: Literal["Credit", "Debit", "Cash", "Online"]


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    card_info: str = None
    transaction_status: str = None
    payment_type: Literal["Credit", "Debit", "Cash", "Online"] = None


class Payment(PaymentBase):
    id: int

    class ConfigDict:
        from_attributes = True