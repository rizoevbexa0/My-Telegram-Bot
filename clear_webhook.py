from aiogram import Bot
from config import TOKEN
import asyncio

async def main():
    bot = Bot(token=TOKEN)
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.session.close()
    print("Webhook удалён, бот можно запускать через polling.")

asyncio.run(main())
