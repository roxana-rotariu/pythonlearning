from sqlalchemy import select
from app.models.user_model import User

class UserRepository:
    async def create(self, db, data):
        user = User(email=data.email, password=data.password)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    async def get_by_email(self, db, email: str):
        result = await db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def get(self, db, user_id: int):
        result = await db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()
