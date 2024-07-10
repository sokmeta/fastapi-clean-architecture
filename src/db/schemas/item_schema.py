from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class ItemBase(BaseModel):
    name: str
    description: str
    price: float
    tax: float
    category_id: int

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    deleted_at: Optional[datetime]

class Item(ItemBase):
    id: int
    deleted_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
