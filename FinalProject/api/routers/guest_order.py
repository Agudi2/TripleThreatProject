from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from ..controllers import guest_order as controller
from ..schemas import guest_order as schema
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/guest_orders",
    tags=["Guest Orders"]
)

@router.post("/", response_model=schema.GuestOrder, status_code=status.HTTP_201_CREATED)
def create_guest_order(request: schema.GuestOrderCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.GuestOrder])
def read_all_guest_orders(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{guest_order_id}", response_model=schema.GuestOrder)
def read_one_guest_order(guest_order_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, guest_order_id)

@router.delete("/{guest_order_id}", response_model=schema.GuestOrder)
def delete_guest_order(guest_order_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, guest_order_id)
