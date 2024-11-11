from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from ..controllers import menu as controller
from ..schemas import menu as schema
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/menu",
    tags=["Menu"]
)

@router.post("/", response_model=schema.MenuItem, status_code=status.HTTP_201_CREATED)
def create_menu_item(request: schema.MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/", response_model=list[schema.MenuItem])
def read_all_menu_items(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{menu_item_id}", response_model=schema.MenuItem)
def read_one_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, menu_item_id)

@router.put("/{menu_item_id}", response_model=schema.MenuItem)
def update_menu_item(menu_item_id: int, request: schema.MenuItemUpdate, db: Session = Depends(get_db)):
    return controller.update(db, menu_item_id, request)

@router.delete("/{menu_item_id}", response_model=schema.MenuItem)
def delete_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, menu_item_id)
