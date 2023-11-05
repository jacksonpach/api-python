from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config.settings import POSTGRES_URL

engine = create_async_engine(POSTGRES_URL, echo=True)

AsyncSession = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
