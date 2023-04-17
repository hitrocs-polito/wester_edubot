import logging

from aiogram import Dispatcher
from aiogram.utils.exceptions import ChatNotFound

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(chat_id=ADMINS[0], text="Bot started")

    except ChatNotFound as err:
        logging.exception(err)
