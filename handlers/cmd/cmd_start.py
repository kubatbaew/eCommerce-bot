from aiogram.types import Message

from aiogram.filters import CommandStart

from handlers.base import router


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать!")
