from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

from requests.category import get_categories
from requests.item import get_item_by_category


async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(
            text=category.title,
            callback_data=f"category_{category.id}",
        ))
    return keyboard.adjust(1).as_markup()


async def items(category_id: int):
    items_by_category = await get_item_by_category(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in items_by_category:
        keyboard.add(InlineKeyboardButton(
            text=item.title,
            callback_data=f"item_{item.id}"
        ))
    return keyboard.adjust(1).as_markup()
