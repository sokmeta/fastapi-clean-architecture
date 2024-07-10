from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.types import ASGIApp
from core.config import SessionLocal


class SessionMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        request.state.session = SessionLocal()
        try:
            response = await call_next(request)
        except Exception as exception:
            request.state.session.rollback()
            request.state.session.close()
            raise exception
        else:
            request.state.session.commit()
        finally:
            request.state.session.close()

        return response
