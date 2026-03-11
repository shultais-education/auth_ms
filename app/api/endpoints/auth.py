from datetime import datetime, timedelta
import jwt
from fastapi import APIRouter, HTTPException

from app.schemas.auth import LoginRequest, TokenResponse, UserResponse
from app.core.config import settings
from app.api.dependencies.security import KeyHeaderDep


auth_router = APIRouter()


users_db = {
    "admin": {"password": "admin123", "role": "admin", "id": 1, "email": "admin@example.com", "first_name": "Админ"},
    "user1": {"password": "user123", "role": "user", "id": 2, "email": "user1@example.com", "first_name": "Никита"},
    "user2": {"password": "user456", "role": "user", "id": 3, "email": "user2@example.com", "first_name": "Алена"},
}

users_by_id = {
    user["id"]: user for username, user in users_db.items()
}



@auth_router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest):
    user = users_db.get(request.username)
    if not user or user["password"] != request.password:
        raise HTTPException(401, detail="Неверный логин или пароль")

    # Создаем JWT токен
    payload = {
        "user_id": user["id"],
        "role": user["role"],
        "exp": datetime.now() + timedelta(hours=24)
    }

    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return {"access_token": token}


@auth_router.get("/{user_id}", response_model=UserResponse)
async def user_detail(user_id: int, api_key: KeyHeaderDep):

    if api_key not in ('AUTH-ABC',):
        raise HTTPException(status_code=401, detail="Неверный ключ")

    user = users_by_id.get(user_id)

    if not user:
        raise HTTPException(403, detail="Пользователь не найден")

    return user
