from fastapi import APIRouter, Query, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated
from db.schemas import UserCreate
from services import AuthService
from dependency import get_db, get_current_user
from utils.token import oauth2_scheme, decode_token
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
    
    token = auth_service.generate_access_token(user.username, user.id)
    refresh_token = auth_service.generate_refresh_token(user.username, user.id)

    return {
        "access_token": token, 
        "refresh_token": refresh_token,
        "token_type": "Bearer"
    }

@router.post("/token/refresh")
async def refresh_token(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = decode_token(token)
        username = payload.get("sub")
        user_id = payload.get("id")
    except HTTPException:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    new_token = auth_service.generate_access_token(username, user_id)
    refresh_token = auth_service.generate_refresh_token(username, user_id)

    return {
        "access_token": new_token, 
        "refresh_token": refresh_token,
        "token_type": "Bearer"
    }

@router.get("/user")
async def get_user(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(401)
    return user