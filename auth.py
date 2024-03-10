from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from security import SECRET_KEY, ALGORITHM
from models import UserDB
from jose import JWTError, jwt
from passlib.context import CryptContext
from database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db, email: str):
    return db.query(UserDB).filter(UserDB.email == email).first()

def get_current_user(token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return email

def get_current_active_user(current_user: str = Depends(get_current_user)):
    return current_user

def authenticate_user(db, username: str, password: str):
    user = db.query(UserDB).filter(UserDB.email == username).first()
    if user is None or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user