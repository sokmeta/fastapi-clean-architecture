from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError, StarletteHTTPException

from routers import item, category, auth
from core.config import PREFIX
from middlewares import SessionMiddleware, LoggingMiddleware
from handler import exception_handler


app = FastAPI()

app.add_middleware(SessionMiddleware)
app.add_middleware(LoggingMiddleware)

app.include_router(item.router, prefix=PREFIX)
app.include_router(category.router, prefix=PREFIX)
app.include_router(auth.router, prefix=PREFIX)


exception_list = [
    HTTPException,
    RequestValidationError,
    StarletteHTTPException,
    Exception
]

for exception in exception_list:
    app.add_exception_handler(exception, exception_handler)