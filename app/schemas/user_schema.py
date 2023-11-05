from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    full_name: Optional[str] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


class UserUpdate(UserBase):
    pass
