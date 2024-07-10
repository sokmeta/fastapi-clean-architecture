from db.repositories.item_repository import ItemRepository
from db.models import ItemModel
from db.schemas import ItemCreate

repository = ItemRepository(ItemModel)

def test_create_item(db):
    item = ItemCreate(name="Item1", description="Description1", price=100.0, tax=10.0, category_id=1)
    created_item = repository.create(db, item)
    assert created_item.name == "Item1"
    assert created_item.description == "Description1"

def test_get_items(db):
    items = repository.get_all(db)
    assert len(items) >= 0
    assert all(isinstance(item, ItemModel) for item in items)

