from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserService:

    @staticmethod
    async def get_all_users(db: AsyncSession):
        result = await db.execute(select(User))
        return result.scalars().all()

    @staticmethod
    async def get_user(db: AsyncSession, user_id: int):
        result = await db.execute(select(User).where(User.id == user_id))
        return result.scalar()

    @staticmethod
    async def create_user(db: AsyncSession, user: UserCreate):
        db_user = User(**user.dict())
        async with db.begin():
            db.add(db_user)
            await db.flush()
            await db.refresh(db_user)
        return db_user

    @staticmethod
    async def update_user(db: AsyncSession, user_id: int, user: UserUpdate):
        db_user = await UserService.get_user(db, user_id)
        for key, value in user.model_dump().items():
            setattr(db_user, key, value)
        await db.commit()
        return db_user

    @staticmethod
    async def delete_user(db: AsyncSession, user_id: int):
        db_user = await UserService.get_user(db, user_id)
        await db.delete(db_user)
        await db.commit()
        return db_user
