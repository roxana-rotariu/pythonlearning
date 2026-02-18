import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_token(user_id: int):
    payload = {"sub": user_id, "exp": datetime.utcnow() + timedelta(hours=1)}
    return jwt.encode(payload, settings.JWT_SECRET, settings.JWT_ALGORITHM)

def decode_token(token: str):
    return jwt.decode(token, settings.JWT_SECRET, settings.JWT_ALGORITHM)
