from core.database import SessionLocal
from utils.token import get_current_user


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()