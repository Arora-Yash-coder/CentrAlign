from fastapi import APIRouter, HTTPException
from fastapi import Depends
from models.user import UserCreate, UserLogin
from services.user_service import (
    create_user,
    authenticate_user,
    generate_jwt_token
)

router = APIRouter()

@router.post("/signup")
def signup(payload: UserCreate):
    user = create_user(payload)
    if not user:
        raise HTTPException(status_code=400, detail="User already exists.")
    return {"status": "success", "message": "Account created successfully"}

@router.post("/login")
def login(payload: UserLogin):
    user = authenticate_user(payload.email, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = generate_jwt_token(user["_id"])
    return {
        "status": "success",
        "token": token,
        "user_id": str(user["_id"])
    }
