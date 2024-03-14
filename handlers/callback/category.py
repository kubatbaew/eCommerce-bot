from aiogram.types import CallbackQuery
from aiogram import F

from handlers.base import router

from keyboards.data import items
from requests.category import get_category_by_id


@router.callback_query(F.data.startswith('category_'))
async def callback_category(callback: CallbackQuery):
    category_id = int(callback.data.split('_')[1])
    category = await get_category_by_id(category_id)

    await callback.answer(f"Вы выбрали: {category.title}")
    await callback.message.answer(
        "Выберите товар...",
        reply_markup=await items(category_id)
    )
