from aiogram.types import Message

from aiogram.filters import CommandStart

from handlers.base import router
from keyboards.main import main_keyboard


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать!", reply_markup=main_keyboard)
