from db.categories import Category
from db.base import async_session

from sqlalchemy import select, update, delete


async def get_categories():
    async with async_session() as session:
        categories = await session.scalars(select(Category))
        return categories


async def get_category_by_id(category_id: int):
    async with async_session() as session:
        category = await session.scalar(select(Category).where(Category.id == category_id))
        return category
