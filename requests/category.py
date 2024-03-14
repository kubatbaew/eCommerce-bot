from db.categories import Category
from db.base import async_session

from sqlalchemy import select, update, delete


async def get_categories():
    async with async_session() as session:
        categories = await session.scalars(select(Category))
        return categories
