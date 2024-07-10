from sqlalchemy.orm import Session
from db.schemas import ItemCreate
from db.repositories import ItemRepository
from db.models import ItemModel

class ItemService:
    def __init__(self, db: Session):
        self.repository = ItemRepository(ItemModel)

    def get_items(self, db: Session):
        return self.repository.get_all(db)

    def get_item_by_id(self, db: Session, id: int):
        return self.repository.get(db, id)

    def create_item(self, db: Session, item: ItemCreate):
        return self.repository.create(db, item)

    def delete_item(self, db: Session, id: int):
        return self.repository.delete(db, id)

    def update_item(self, db: Session, id: int, item: ItemCreate):
        return self.repository.update(db, id, item)
