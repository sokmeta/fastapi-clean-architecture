from sqlalchemy import Column, Integer, DateTime, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db.base import Base


class ItemModel(Base):

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column("name", String(200), nullable=False)
    description = Column("description", String(1000), nullable=False)
    price = Column("price", Float, nullable=False)
    tax = Column("tax", Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    deleted_at = Column("deleted_at", DateTime(timezone=False), nullable=True)

    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("CategoryModel", back_populates="items")
