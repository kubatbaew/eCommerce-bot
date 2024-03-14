from db.items import Item
from db.base import async_session

from sqlalchemy import select, update, delete


async def get_item_by_category(category_id: int):
    async with async_session() as session:
        items = await session.scalars(select(Item).where(Item.category == category_id))
        return items
