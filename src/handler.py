# error_handlers.py
import json
import traceback
from fastapi import Request, HTTPException
from fastapi.exceptions import RequestValidationError, StarletteHTTPException
from fastapi.responses import JSONResponse
from logger import logger


LOG_FORMAT = 'json'

async def exception_handler(request: Request, exception: Exception):
    error_log = {
        "url": request.url.path,
        "message": f"{exception}",
    }

    if isinstance(exception, HTTPException) and exception.status_code < 500:
        error_log["status_code"] = exception.status_code
    else:
        error_log["backtrace"] = list(traceback.TracebackException.from_exception(exception).format())

    if LOG_FORMAT == 'json':
        logger.error(json.dumps(error_log))
    else:
        traceback.print_exc()

    return handle_error_response(request, exception)

def handle_error_response(request: Request, exception: Exception):
    # Default error response
    status_code = 500
    detail = "An internal server error occurred."

    if isinstance(exception, HTTPException):
        status_code = exception.status_code
        detail = exception.detail

    elif isinstance(exception, RequestValidationError):
        status_code = 422
        detail = exception.errors()

    elif isinstance(exception, StarletteHTTPException):
        status_code = exception.status_code
        detail = exception.detail

    # Custom response for different error formats
    if LOG_FORMAT == 'json':
        response_content = {
            "error": {
                "type": type(exception).__name__,
                "message": detail,
                "status_code": status_code
            }
        }
    else:
        response_content = {
            "detail": detail
        }

    return JSONResponse(status_code=status_code, content=response_content)