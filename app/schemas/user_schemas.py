from pydantic import BaseModel
from app.models import UserRole

class UserCreate(BaseModel):
    name: str
    password: str
    email: str
    role: UserRole = UserRole.customer

class UserPublic(BaseModel):
    name: str
    email: str
    role: UserRole

class UserPrivate(UserPublic):
    password_hash: str