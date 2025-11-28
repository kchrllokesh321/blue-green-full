from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://45.129.86.68",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(data: LoginRequest):
    if data.username == "admin" and data.password == "admin":
        return {"status": "ok", "message": "Login success"}
    return {"status": "error", "message": "Invalid credentials"}
