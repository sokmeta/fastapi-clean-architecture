from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from typing import Annotated
from db.schemas import CategoryBase
from services import CategoryService
from dependency import get_db, get_current_user

router = APIRouter(prefix="/categories", tags=["Category"], dependencies=[Depends(get_current_user)])
category_service = CategoryService

@router.get("/", description="Get all Items", response_model=list[CategoryBase])
def get_items(search: Annotated[str | None, Query(max_length=50)] = None, db: Session = Depends(get_db)):
    return category_service(db).get_items(db)

@router.get("/{id}", description="Get Item by ID", response_model=CategoryBase)
def get_item_by_id(id: int, db: Session = Depends(get_db)):
    return category_service(db).get_item_by_id(db, id)

@router.post("/create", description="Create an Item", response_model=CategoryBase)
def create(body: CategoryBase, db: Session = Depends(get_db)):
    return category_service(db).create_item(db, body)

@router.delete("/delete/{id}", description="Delete Item by ID")
def delete(id: int, db: Session = Depends(get_db)):
    return category_service(db).delete_item(db, id)

@router.put("/update/{id}", description="Update Item", response_model=CategoryBase)
def update(id: int, body: CategoryBase, db: Session = Depends(get_db)):
    return category_service(db).update_item(db, id, body)