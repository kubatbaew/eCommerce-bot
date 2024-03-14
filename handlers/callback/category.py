from aiogram.types import CallbackQuery
from aiogram import F

from handlers.base import router


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer("Выберите товар...")
