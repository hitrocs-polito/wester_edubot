from aiogram import types

from data.config import ADMINS
from loader import dp, bot, db


@dp.message_handler(text="📞 Mutaxassis bilan aloqa")
async def aloqa(message: types.Message):
    await message.answer("✅ So'rov qabul qilindi.\n\n"
                         f"Mutaxassislarimiz {db.get_number(message.from_user.id)[0]} \n"
                         f"raqamingizga tez orada bog'lanishadi.")
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"#aloqa\n"
                                f"Foydalanuvchi:\n\n"
                                f"Ismi: {db.get_firstname(message.from_user.id)[0]}\n"
                                f"Familiya: {db.get_lastname(message.from_user.id)[0]}\n"
                                f"Nomeri: {db.get_number(message.from_user.id)[0]}\n"
                                f"Mutaxassis bilan bog'lanishni tanladi.")
