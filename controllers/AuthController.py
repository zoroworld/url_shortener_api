from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models import User, Token
from models.db import db_users
from utils.TokenUtil import create_access_token

router = APIRouter()



@router.post("/register")
async def register(user: User):
    if user.username in db_users:
        raise HTTPException(status_code=400, detail="Username exists")
    db_users[user.username] = user
    return {"msg": "User registered"}

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db_users.get(form_data.username)
    if not user or user.password != form_data.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
