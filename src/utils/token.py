from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError, ExpiredSignatureError
from core.config import SCRET_KEY, ALGORITHM, PREFIX

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{PREFIX}/auth/token")

def generate_token(name, id, expires_minutes):
    encode = {"sub": name, "id": id}
    expires = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    encode.update({"exp": expires})
    return jwt.encode(encode, SCRET_KEY, algorithm=ALGORITHM)

def decode_token(token):
    try:
        return jwt.decode(token, SCRET_KEY, algorithms=[ALGORITHM])
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

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