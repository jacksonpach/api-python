from typing import Optional

from pydantic import BaseModel, field_validator, EmailStr


class UserBase(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None

    @field_validator('email')
    def check_email(cls, v):
        if v is not None and '@' not in v:
            raise ValueError('Invalid email address')
        return v


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


class UserUpdate(UserBase):
    pass
