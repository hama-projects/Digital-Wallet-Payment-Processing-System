from fastapi import APIRouter
from backend.services.auth_service import create_user, authenticate_user

router = APIRouter()


@router.post("/register")
def register_user(username: str, password: str):
    user = create_user(username, password)
    return {"message": "User created", "user": user}


@router.post("/login")
def login(username: str, password: str):
    result = authenticate_user(username, password)

    if not result:
        return {"error": "Invalid credentials"}

    return {"message": "Login successful", "user": result}