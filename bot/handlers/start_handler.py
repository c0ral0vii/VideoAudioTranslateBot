from aiogram import Router, types
from aiogram.filters import Command
from loguru import logger
from bot.kb.main_keyboard import main_kb
from bot.utils.messages import START_MESSAGE
from db.dals import UserDAL

router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message):
    """start_handler"""

    logger.info(f"Пользователь - {message.from_user.id} написал /start")
    await message.answer(START_MESSAGE, reply_markup=await main_kb())
    