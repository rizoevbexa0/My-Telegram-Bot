from aiogram import Router
from aiogram.types import Message

from db import get_role

router = Router()


@router.message(lambda m: m.text == "📌 Помощь")
async def help_by_role(message: Message):
    role = get_role(message.from_user.id)

    if role is None:
        await message.answer("❗ Сначала выбери роль через /start")
        return

    texts = {
        "🎓 Студент": "📚 Я помогу с учёбой, планированием и мотивацией.",
        "💼 Работа": "🗂 Помогу с задачами, приоритетами и фокусом.",
        "🧠 Саморазвитие": "🔥 Привычки, цели, рост каждый день.",
        "💰 Финансы": "💵 Учёт расходов, цели, контроль.",
        "🧘 Здоровье": "💪 Сон, вода, режим, самочувствие."
    }

    await message.answer(texts.get(role, "🤖 Я рядом, чем помочь?"))
