from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from .routers import users_router

app = FastAPI()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="get-token")

app.include_router(users_router)