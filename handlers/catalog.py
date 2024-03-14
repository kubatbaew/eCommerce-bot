from handlers.base import router
from aiogram.types import Message, CallbackQuery
from aiogram import F

from keyboards.data import categories


@router.message(F.text == "Каталог")
async def catalog(message: Message):
    await message.answer("Выберите категорию.", reply_markup=await categories())
