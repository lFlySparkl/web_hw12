from sqlalchemy.orm import Session
from models import UserDB
from passlib.context import CryptContext
from pydantic_models import UserCreate


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, user_id: int):
    return db.query(UserDB).filter(UserDB.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(UserDB).filter(UserDB.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = UserDB(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
