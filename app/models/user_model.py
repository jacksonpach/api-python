from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(200), unique=True, index=True)
    email = Column(String(200), unique=True, index=True)
    full_name = Column(String(255), index=True)
