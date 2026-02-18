from fastapi import HTTPException
from app.repository.user_repo import UserRepository
from app.core.security import hash_password, verify_password

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    async def register(self, db, user_data):
        exists = await self.repo.get_by_email(db, user_data.email)
        if exists:
            raise HTTPException(status_code=400, detail="Email already exists")
        user_data.password = hash_password(user_data.password)
        return await self.repo.create(db, user_data)

    async def authenticate(self, db, email: str, password: str):
        user = await self.repo.get_by_email(db, email)
        if not user or not verify_password(password, user.password):
            raise HTTPException(status_code=400, detail="Invalid credentials")
        return user
