from sqlalchemy import Column, Integer, String, DateTime
from db.base import Base
from datetime import datetime

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(200), unique=True, index=True, nullable=False)
    email = Column("email", String(319), index=True)
    password = Column("password", String(255))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    deleted_at = Column("deleted_at", DateTime(timezone=False), nullable=True)