from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from core.config import SCRET_KEY, ALGORITHM, PREFIX

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{PREFIX}/auth/token")

def generate_token(name, id):
    encode = {"sub": name, "id": id}
    expires = datetime.now() + timedelta(minutes=20)
    encode.update({"exp": expires})
    return jwt.encode(encode, SCRET_KEY, algorithm=ALGORITHM)

def decode_token(token):
    return jwt.decode(token, SCRET_KEY, algorithms=[ALGORITHM])


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = decode_token(token)
        username = payload.get("sub")
        user_id = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(detail="Could not validate user")
        
        return {
            "username": username,
            "user_id": user_id
        }
    except JWTError:
        raise HTTPException(detail="Could not validate user")