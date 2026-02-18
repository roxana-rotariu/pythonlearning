from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.user_schema import UserCreate, UserRead

router = APIRouter()

fake_db = []
current_id = 1

@router.post("/users", response_model=UserRead)
async def create_user(user: UserCreate):
    global current_id
    new_user = UserRead(id=current_id, name=user.name)
    fake_db.append(new_user)
    current_id += 1
    return new_user

@router.get("/users", response_model=List[UserRead])
async def list_users():
    return fake_db

@router.get("/users/{user_id}", response_model=UserRead)
async def get_user(user_id: int):
    for user in fake_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
