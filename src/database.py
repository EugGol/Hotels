from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from config import settings

engine = create_async_engine(settings.DB_URL)

async_sessionmaker_maker = async_sessionmaker(bind=engine, expire_on_commit=False)

session = async_sessionmaker_maker()


class Base(DeclarativeBase):
    pass    