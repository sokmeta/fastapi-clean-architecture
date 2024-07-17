from sqlalchemy.orm import Session
from db.schemas import ItemCreate
from db.repositories import ItemRepository
from db.models import ItemModel
from cache import Memcache

cache = Memcache()

class ItemService:
    def __init__(self, db: Session):
        self.repository = ItemRepository(ItemModel)

    def get_items(self, db: Session):
        return self.repository.get_all(db)

    def get_item_by_id(self, db: Session, id: int):
        cached_item = cache.get_vars(f"item_{id}")
        if cached_item: 
            return cached_item

        item = self.repository.get(db, id)
        cache.set_vars(f"item_{id}", item)
        return item

    def create_item(self, db: Session, item: ItemCreate):
        new_item = self.repository.create(db, item)
        cache.set_vars(f"item_{new_item.id}", new_item)
        return new_item

    def delete_item(self, db: Session, id: int):
        cache.delete(f"item_{id}")
        return self.repository.delete(db, id)

    def update_item(self, db: Session, id: int, item: ItemCreate):
        updated_item = self.repository.update(db, id, item)
        cache.set_vars(f"item_{id}", updated_item)
        return updated_item
    