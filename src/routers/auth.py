from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from db.schemas import UserCreate
from services import AuthService
from dependency import get_db, get_current_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Auth"])
auth_service = AuthService

@router.post("/create_user")
async def create_user(body: UserCreate, db: Session = Depends(get_db)):
    return auth_service.create_user(db, body)


@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = auth_service.authenticate(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(401)
    
    token = auth_service.create_token(user.username, user.id)

    return {"access_token": token, "token_type": "Bearer"}

@router.get("/user")
async def get_user(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(401)
    return user