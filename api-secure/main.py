# api-secure/main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
security = HTTPBearer()

USERS = {
    1: {"id": 1, "username": "admin", "role": "admin"},
    2: {"id": 2, "username": "user", "role": "user"},
}

def check_token(creds: HTTPAuthorizationCredentials = Depends(security)):
    if creds.credentials != "secure-admin-token":
        raise HTTPException(status_code=403, detail="Forbidden")
    return True

@app.get("/users/{user_id}")
def get_user(user_id: int, auth=Depends(check_token)):
    if user_id not in USERS:
        raise HTTPException(404)
    return USERS[user_id]