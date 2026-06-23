from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from app.crud import sign_up, sing_in
from app.schemas import UserCreate
from typing import Annotated

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/sign-up")
async def sign_up_r(data: UserCreate):
    sign_up(data)
    return JSONResponse(status_code=201, content={"message": "User created successfully"})

@router.get("/sign-in")
async def sign_in_r(data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    token = sing_in(data)
    return token