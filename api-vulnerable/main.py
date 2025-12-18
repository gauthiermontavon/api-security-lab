# api-vulnerable/main.py
from fastapi import FastAPI, Request

app = FastAPI()

USERS = [
    {"id": 1, "username": "admin", "role": "admin"},
    {"id": 2, "username": "user", "role": "user"},
    {"id": 3, "username": "user1", "role": "user"}
]

@app.get("/users")
def get_users():
    # ❌ Excessive Data Exposure
    return USERS

@app.get("/users/{user_id}")
def get_user(user_id: int):
    # ❌ BOLA (Broken Object Level Authorization)
    return USERS[user_id - 1]

@app.post("/login")
async def login(request: Request):
    data = await request.json()
    # ❌ Auth totalement cassée
    return {"token": f"token-{data['username']}"}