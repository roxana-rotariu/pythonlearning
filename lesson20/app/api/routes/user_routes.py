from fastapi import APIRouter, Depends
from app.core.database import get_db          # ✅ core.database
from app.schemas.user_schema import UserCreate, UserRead
from app.services.user_service import UserService
from app.core.security import create_token

router = APIRouter(prefix="/users")
service = UserService()

@router.post("/register", response_model=UserRead)
async def register(user: UserCreate, db=Depends(get_db)):
    return await service.register(db, user)

@router.post("/login")
async def login(user: UserCreate, db=Depends(get_db)):
    auth_user = await service.authenticate(db, user.email, user.password)
    token = create_token(auth_user.id)
    return {"token": token}
