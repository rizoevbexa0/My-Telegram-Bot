from aiogram import Bot, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👋 Привет"), KeyboardButton(text="❓ Помощь")],
        [KeyboardButton(text="🧑 Выбрать роль"), KeyboardButton(text="📝 Моя роль")]
    ],
    resize_keyboard=True
)

role_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Junior"), KeyboardButton(text="Middle")],
        [KeyboardButton(text="Senior"), KeyboardButton(text="Teamlead")]
    ],
    resize_keyboard=True
)
