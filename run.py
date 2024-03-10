import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from config import BOT_TOKEN

from handlers.base import router
from db.base import async_main


async def main():
    await async_main()
    bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        print("[NOTIFICATION!]: Starting bot")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("[NOTIFICATION!]: Stop bot")
