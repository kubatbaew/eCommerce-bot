from aiogram.types import Message

from aiogram.filters.command import CommandStart, Command
from aiogram import Router

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать!")
