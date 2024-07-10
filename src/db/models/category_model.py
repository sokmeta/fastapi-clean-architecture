from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from db.base import Base

class CategoryModel(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    deleted_at = Column("deleted_at", DateTime(timezone=False), nullable=True)

    items = relationship("ItemModel", back_populates="category")