import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from src.config import settings
from src.handlers import router

load_dotenv()

TOKEN = settings.BOT_TOKEN

dp = Dispatcher()
dp.include_router(router)


async def main():
    bot = Bot(token=TOKEN)  # type: ignore
    await dp.start_polling(bot)  # type: ignore


if __name__ == "__main__":
    asyncio.run(main())
