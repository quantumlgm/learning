from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str 


class UserOut(BaseModel):
    id: int
    email: EmailStr
    username: str
    is_active: bool = True

    class Config:
        from_attributes = True


class UserInDB(BaseModel):
    id: int
    email: EmailStr
    username: str
    hashed_password: str 
    is_active: bool = True