from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession as SqlAlchemyAsyncSession

from app.database.session import AsyncSession as AsyncBase
from app.schemas.user_schema import User as UserSchema, UserCreate, UserUpdate
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


async def get_db_session():
    session = AsyncBase()
    try:
        yield session
    finally:
        await session.close()


def ensure_found(user, detail: str = "Item not found"):
    """Ensure the item is not None or raises an HTTP exception."""
    if not user:
        raise HTTPException(status_code=404, detail=detail)
    return user


@router.get("/", response_model=list[UserSchema])
async def read_users(db: SqlAlchemyAsyncSession = Depends(get_db_session)):
    users = await UserService.get_all_users(db)
    ensure_found(users, "No users found.")
    return users


@router.get("/{user_id}", response_model=UserSchema)
async def read_user(user_id: int, db: SqlAlchemyAsyncSession = Depends(get_db_session)):
    user = await UserService.get_user(db, user_id)
    ensure_found(user, f"User with ID {user_id} not found.")
    return user


@router.post("/", response_model=UserSchema)
async def create_user(user: UserCreate, db: SqlAlchemyAsyncSession = Depends(get_db_session)):
    user = await UserService.create_user(db, user)
    ensure_found(user, "Failed to create user.")
    return user


@router.put("/{user_id}", response_model=UserUpdate)
async def update_user(user_id: int, user: UserUpdate, db: SqlAlchemyAsyncSession = Depends(get_db_session)):
    updated_user = await UserService.update_user(db, user_id, user)
    ensure_found(updated_user, f"Failed to update user with ID {user_id}.")
    return updated_user


@router.delete("/{user_id}", response_model=UserSchema)
async def delete_user(user_id: int, db: SqlAlchemyAsyncSession = Depends(get_db_session)):
    deleted_user = await UserService.delete_user(db, user_id)
    ensure_found(deleted_user, f"Failed to delete user with ID {user_id}.")
    return deleted_user
