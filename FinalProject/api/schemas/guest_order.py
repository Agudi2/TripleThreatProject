from pydantic import BaseModel

class GuestOrderBase(BaseModel):
    customer_name: str
    phone: str
    address: str
    order_description: str

class GuestOrderCreate(GuestOrderBase):
    pass

class GuestOrder(GuestOrderBase):
    id: int

    class Config:
        orm_mode = True
