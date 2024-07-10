from .base import BaseRepository
from db.models import ItemModel
from db.schemas import ItemCreate

class ItemRepository(BaseRepository[ItemModel, ItemCreate]):
    pass