from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    age: int

class UserRead(BaseModel):
    id: int
    name: str
