from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.config import ADMINS
from loader import dp


@dp.message_handler(CommandHelp(), user_id=ADMINS)
async def get_info(message: types.Message):
    await message.answer(f"Reklama - /reklama\n"
                         f"Userlar soni - /allusers\n"
                         f"Userlar ro'yxati - /userlar\n"
                         f"Help - /help")