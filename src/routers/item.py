from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from typing import Annotated
from db.schemas import ItemBase as ItemInterface, ItemCreate
from services import ItemService
from dependency import get_db

router = APIRouter(prefix="/items", tags=["Item"])
item_service = ItemService

@router.get("/", description="Get all Items", response_model=list[ItemInterface])
def get_items(search: Annotated[str | None, Query(max_length=50)] = None, db: Session = Depends(get_db)):
    return item_service(db).get_items(db)

@router.get("/{id}", description="Get Item by ID", response_model=ItemInterface)
def get_item_by_id(id: int, db: Session = Depends(get_db)):
    return item_service(db).get_item_by_id(db, id)

@router.post("/create", description="Create an Item", response_model=ItemInterface)
def create(body: ItemCreate, db: Session = Depends(get_db)):
    return item_service(db).create_item(db, body)

@router.delete("/delete/{id}", description="Delete Item by ID")
def delete(id: int, db: Session = Depends(get_db)):
    return item_service(db).delete_item(db, id)

@router.put("/update/{id}", description="Update Item", response_model=ItemInterface)
def update(id: int, body: ItemCreate, db: Session = Depends(get_db)):
    return item_service(db).update_item(db, id, body)