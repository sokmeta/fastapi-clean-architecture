from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.types import ASGIApp
from logger import logger
import time


class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)

        process_time = time.time() - start
        logging_dict = {
            "url": request.url.path,
            "method": request.method,
            "status_code": response.status_code,
            "process_time": process_time
        }
        logger.info(logging_dict)

        return response