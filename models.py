from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date
from pydantic import BaseModel

Base = declarative_base()

class ContactDB(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    phone_number = Column(String)
    hashed_password = Column(String)
    birthday = Column(Date)
    additional_data = Column(String, nullable=True)

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True, unique=True)
    hashed_password = Column(String)

class Token(BaseModel):
    access_token: str
    token_type: str