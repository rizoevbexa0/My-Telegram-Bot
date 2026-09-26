from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from db import set_role

router = Router()

role_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎓 Студент")],
        [KeyboardButton(text="💼 Работа")],
        [KeyboardButton(text="🧠 Саморазвитие")],
        [KeyboardButton(text="💰 Финансы")],
        [KeyboardButton(text="🧘 Здоровье")],
    ],
    resize_keyboard=True
)


@router.message(F.text.in_([
    "🎓 Студент",
    "💼 Работа",
    "🧠 Саморазвитие",
    "💰 Финансы",
    "🧘 Здоровье"
]))
async def choose_role(message: Message):
    role = message.text
    set_role(message.from_user.id, role)

    await message.answer(
        f"✅ Роль сохранена: {role}\n\n"
        "Теперь бот будет помогать тебе по этой теме.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📌 Помощь")],
                [KeyboardButton(text="🔄 Сменить роль")]
            ],
            resize_keyboard=True
        )
    )
