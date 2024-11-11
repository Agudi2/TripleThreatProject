from sqlalchemy.orm import Session
from ..models import guest_order as model
from ..schemas import guest_order as schema

def create(db: Session, guest_order: schema.GuestOrderCreate):
    db_guest_order = model.GuestOrder(**guest_order.dict())
    db.add(db_guest_order)
    db.commit()
    db.refresh(db_guest_order)
    return db_guest_order

def read_all(db: Session):
    return db.query(model.GuestOrder).all()

def read_one(db: Session, guest_order_id: int):
    return db.query(model.GuestOrder).filter(model.GuestOrder.id == guest_order_id).first()

def delete(db: Session, guest_order_id: int):
    db_guest_order = db.query(model.GuestOrder).filter(model.GuestOrder.id == guest_order_id).first()
    db.delete(db_guest_order)
    db.commit()
    return db_guest_order
