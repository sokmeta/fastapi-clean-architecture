from fastapi import FastAPI
from routers import item, category
from db.base import Base
from core.config import PREFIX, engine
from middlewares import SessionMiddleware
from contextlib import asynccontextmanager



@asynccontextmanager
async def lifespan(application: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(SessionMiddleware)

app.include_router(item.router, prefix=PREFIX)
app.include_router(category.router, prefix=PREFIX)

# @app.on_event("startup")
# async def on_startup():
#     Base.metadata.create_all(bind=engine)

