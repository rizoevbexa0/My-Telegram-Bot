import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers import start, roles, messages 

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(roles.router)
    dp.include_router(messages.router)

    await dp.start_polling(bot)
    print(" Бот запущен и готов принимать сообщения!")

if __name__ == "__main__":
    asyncio.run(main())
