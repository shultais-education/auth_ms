from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    first_name: str
    email: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
