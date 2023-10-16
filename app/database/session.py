from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config.settings import DB_URL_ASYNCMY

engine = create_async_engine(DB_URL_ASYNCMY, echo=True)
AsyncSession = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
