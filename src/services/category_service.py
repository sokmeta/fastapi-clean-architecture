from sqlalchemy.orm import Session
from db.schemas import CategoryBase
from db.repositories import CategoryRepository
from db.models import CategoryModel

class CategoryService:
    def __init__(self, db: Session):
        self.repository = CategoryRepository(CategoryModel)

    def get_items(self, db: Session):
        return self.repository.get_all(db)

    def get_item_by_id(self, db: Session, id: int):
        return self.repository.get(db, id)

    def create_item(self, db: Session, item: CategoryBase):
        return self.repository.create(db, item)

    def delete_item(self, db: Session, id: int):
        return self.repository.delete(db, id)

    def update_item(self, db: Session, id: int, item: CategoryBase):
        return self.repository.update(db, id, item)
