from fastapi import FastAPI
from routers import item, category
from core.config import PREFIX
from middlewares import SessionMiddleware


app = FastAPI()

app.add_middleware(SessionMiddleware)

app.include_router(item.router, prefix=PREFIX)
app.include_router(category.router, prefix=PREFIX)
