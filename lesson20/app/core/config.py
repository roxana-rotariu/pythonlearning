from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///./db.sqlite3"
    JWT_SECRET: str = "super-secret"
    JWT_ALGORITHM: str = "HS256"

    model_config = {
        "env_file": ".env"
    }

settings = Settings()
