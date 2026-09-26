from aiogram import types
from aiogram.filters import Command
from loader import dp
from config import ADMIN_ID
from db import session, User

@dp.message(Command("users"))
async def users_command(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("❌ У тебя нет доступа")
        return
    users_list = session.query(User).all()
    if not users_list:
        await message.answer("Пока нет зарегистрированных пользователей")
        return
    text = "Список пользователей:\n"
    for user in users_list:
        role = user.role if user.role else "Не выбрана"
        text += f"- @{user.username} (ID: {user.id}), роль: {role}\n"
    await message.answer(text)
