from aiogram import types
from aiogram.types import CallbackQuery

from data.config import ADMINS
from keyboards.default.homepage_keyboard import menu
from keyboards.inline.inline_phone import inline_pm
from loader import bot, db, dp


@dp.message_handler(text="🏫 Prezident maktabi")
async def bot_start(message: types.Message):
    await message.answer("Farzandingiz prezident boʻlsin!\n\n "
                         "🧐 Farzandlaringiz prezident va ixtisoslashtirilgan maktablarda o’qishini istaysizmi?\n\n"
                         "📈 Buning uchun farzandingiz sifatli ta’lim olishini va doimiy bilimini tekshirib, nazorat qilib borishingiz lozim.\n\n"
                         "✅ Bu ishni WESTER Schoolga topshirishingiz mumkin. Sinalgan uslub va maxsus dastur asosida yuqori natijaga olib chiqamiz.\n\n"
                         "🔵  Prezident maktabiga tayyorlov kurslari uchun bepul kirish imtihonlariga roʻyxatdan oʻtkazing.\n\n"
                         "@wester_kids", reply_markup=inline_pm)


@dp.callback_query_handler(text='pm')
async def backend_true(call: CallbackQuery):
    await call.message.answer("✅ Qabul qilindi.\n\nMutaxassislarimiz tez orada siz bilan bog'lanishadi.",
                              reply_markup=menu)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"#registration_pm\n"
                                f"Foydalanuvchi:\n\n"
                                f"Ismi: {db.get_firstname(call.from_user.id)[0]}\n"
                                f"Familiya: {db.get_lastname(call.from_user.id)[0]}\n"
                                f"Nomeri: {db.get_number(call.from_user.id)[0]}\n"
                                f"Kurs nomi: Prezident maktabi")
    await call.message.delete()
    await call.answer(cache_time=60)
