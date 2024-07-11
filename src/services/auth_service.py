from sqlalchemy.orm import Session
from db.schemas import UserCreate
from db.models import UserModel
from utils.password import pwd_context, verify_password
from utils.token import generate_token

class AuthService:

    def create_user(db: Session, body: UserCreate):
        user = UserModel(
            username = body.username,
            email = body.email,
            password = pwd_context.hash(body.password)
        )

        db.add(user)
        db.commit()

    def authenticate(db: Session, username: str, password: str):
        user = db.query(UserModel).filter(UserModel.username == username).first()
        if not user: return False
        if not verify_password(password, user.password): False

        return user
    
    def create_token(name, id):
        return generate_token(name, id)