from fastapi import FastAPI
from app.api.endpoints.auth import auth_router


app = FastAPI(root_path="/api/users")
app.include_router(auth_router)
