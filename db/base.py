from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from config import ENGINE, ECHO

engine = create_async_engine(url=ENGINE, echo=ECHO)

async_session = async_sessionmaker(engine)


class BaseModel(AsyncAttrs, DeclarativeBase):
    ...


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
