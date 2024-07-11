from fastapi import FastAPI
from routers import item, category
from db.base import Base
from core.config import PREFIX, engine
from middlewares import SessionMiddleware
from contextlib import asynccontextmanager


app = FastAPI()

app.add_middleware(SessionMiddleware)

app.include_router(item.router, prefix=PREFIX)
app.include_router(category.router, prefix=PREFIX)
