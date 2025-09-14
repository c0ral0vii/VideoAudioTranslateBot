from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def main_kb() -> ReplyKeyboardMarkup:
    """main kb creator"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("📚 Каталог сессий")],
            [KeyboardButton("👤 Создать сессию"), KeyboardButton("📋 Мои сессии")],
            [KeyboardButton("👤 Профиль")]
        ],
        resize_keyboard=True
    )