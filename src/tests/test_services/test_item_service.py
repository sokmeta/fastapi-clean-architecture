from services.item_service import ItemService
from db.schemas import ItemCreate
from db.models import ItemModel
from db.repositories import ItemRepository

item_service = ItemService(ItemRepository(ItemModel))


def test_create_item(db):
    item_data = ItemCreate(name="TestItem", description="TestDescription", price=100.0, tax=10.0, category_id=1)
    item = item_service.create_item(db, item_data)
    assert item.name == "TestItem"
    assert item.description == "TestDescription"
    assert item.price == 100.0
    assert item.tax == 10.0

def test_get_items(db):
    items = item_service.get_items(db)
    assert len(items) >= 0
    assert all(isinstance(item, ItemModel) for item in items)