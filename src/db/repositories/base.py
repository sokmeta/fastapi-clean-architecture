from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import Type, TypeVar, Generic, List, Optional
from pydantic import BaseModel
from db.base import Base
from datetime import datetime

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)

class BaseRepository(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: int) -> Optional[ModelType]:
        result = db.query(self.model).filter(
            self.model.id == id,
            self.model.deleted_at == None
        ).first()

        if result is None:
            raise HTTPException(status_code=404, detail="Record not found")

        return result

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return db.query(self.model).filter(self.model.deleted_at == None).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = obj_in.model_dump()
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, id: int, obj_in: CreateSchemaType) -> ModelType:
        db_obj = self.get(db, id)
        update_data = obj_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)   

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        
        return db_obj

    def delete(self, db: Session, id: int) -> None:
        obj = self.get(db, id)
        if obj:
            obj.deleted_at = datetime.now()
            db.add(obj)
            db.commit()