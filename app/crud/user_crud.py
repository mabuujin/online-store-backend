from app.database import get_session
from app.schemas import UserCreate
from app.models import User, UserRole
from app.utilities import get_access_token, authenticate_user
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
import bcrypt
from typing import Annotated
from sqlalchemy import select


def sign_up(data: UserCreate):
    with get_session() as session:
        if data.role == UserRole.admin:
            raise HTTPException(status_code=403, detail="You are Forbidden from performing this operation")

        s = bcrypt.gensalt()
        pw = data.password.encode("utf-8")
        pw_hash = bcrypt.hashpw(pw, s)
        pw_db = pw_hash.decode("utf-8")
        
        user = User(
            name = data.name,
            password_hash = pw_db,
            email = data.email,
            role = data.role
        )

        session.add(user)
        session.commit()
    
def sing_in(data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    with get_session() as session:
        stmt = select(User).where(User.name == data.username)
        user = session.scalar(stmt)
        if authenticate_user(data, user) == False:
            raise HTTPException(status_code=401, detail="Invalid username or password")
        token = get_access_token(data, user)
        return token