from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from db import add_user, get_role, clear_role
from .roles import role_kb

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    user_id = message.from_user.id
    add_user(user_id)

    role = get_role(user_id)

    if role is None:
        await message.answer(
            "👋 Привет!\n\n"
            "Ты ещё не выбрал роль.\n"
            "Выбери, чем тебе помочь:",
            reply_markup=role_kb
        )
    else:
        await message.answer(
            f"👋 Привет!\n\n"
            f"Твоя текущая роль: {role}\n"
            "Нажми «📌 Помощь» или «🔄 Сменить роль»"
        )


@router.message(lambda m: m.text == "🔄 Сменить роль")
async def change_role(message: Message):
    clear_role(message.from_user.id)
    await message.answer(
        "♻️ Роль сброшена.\nВыбери новую:",
        reply_markup=role_kb
    )
