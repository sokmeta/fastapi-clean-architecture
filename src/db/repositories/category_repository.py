from .base import BaseRepository
from db.models import CategoryModel
from db.schemas import CategoryBase

class CategoryRepository(BaseRepository[CategoryModel, CategoryBase]):
    pass