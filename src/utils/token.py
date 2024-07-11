from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from core.config import SCRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def generate_token(name, id):
    encode = {"sub": name, "id": id}
    expires = datetime.now() + timedelta(minutes=20)
    encode.update({"exp": expires})
    return jwt.encode(encode, SCRET_KEY, algorithm=ALGORITHM)