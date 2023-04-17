import re

import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default.contact import contact_keyboard
from keyboards.default.homepage_keyboard import menu
from loader import dp, db, bot
from states.PersonalData import PersonalData


@dp.message_handler(Command('start'))
async def anketa_form(message: types.Message):
    if db.is_exists(message.from_user.id):
        await message.answer("Quyidagi tugmalar orqali o'zingizga kerakli bo'limni tanlang.", disable_web_page_preview=True, reply_markup=menu)
    else:
        await message.answer(
        f"Assalom alaykum!"
        f" <b>Wester School</b>ning rasmiy telegram botiga xush kelibsiz!\n\n"
        f"Botdan foydalanish uchun iltimos ismingizni yozib yuboring.", reply_markup=ReplyKeyboardRemove())

        await PersonalData.first_name.set()


@dp.message_handler(state=PersonalData.first_name)
async def answer_name(message: types.Message, state: FSMContext):
    first_name = re.match('^[A-Za-z]{2,30}$', message.text)
    name = message.text
    if first_name:
        await state.update_data(
            {'first_name': name}
        )
        data = await state.get_data()
        await message.answer(f"Ajoyib, <b>{data.get('first_name')}</b>.\n"
                             f"Iltimos familyangizni yozib yuboring.")
        await PersonalData.next()
    else:
        await message.answer("Iltimos faqat ismingizni kiriting!")



@dp.message_handler(state=PersonalData.last_name)
async def answer_name(message: types.Message, state: FSMContext):
    surname = re.match('^[A-Za-z]{2,30}$', message.text)
    last_name = message.text
    if surname:
        await state.update_data(
            {'last_name': last_name}
        )
        data = await state.get_data()
        await message.answer(f"Tanishganimdan xursandman <b>{data.get('first_name')} {data.get('last_name')}</b>.\n"
                             f"Endi quyidagi tugma orqali telefon raqamingizni ulashsangiz bo'ldi.",
                             reply_markup=contact_keyboard)
        await PersonalData.next()
    else:
        await message.answer("Iltimos faqat familyangizni kiriting!")


@dp.message_handler(content_types=['contact'], state=PersonalData.phone_number)
async def answer_name(message: types.Message, state: FSMContext):
    phone_num = message.contact.phone_number

    await state.update_data(
        {'phone_number': phone_num}
    )

    data = await state.get_data()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phone_number = data.get('phone_number')

    # adding new user's infos to the database
    try:
        db.add_user(message.from_user.id, first_name, last_name, phone_number)
    except asyncpg.exceptions.UniqueViolationError:
        await db.select_user(message.from_user.id)

    text = f"#yangi_user\n"
    text += f"Ismi: {first_name}\n"
    text += f"Familiya: {last_name}\n"
    text += f"Nomeri: {phone_num}\n"

    # Replace the message_id with the ID of a message in the group chat

    await message.answer("✅ Tabriklaymiz, muvaffaqiyatli ro'yxatdan o'tdingiz.\n\n"
                         "Quyidagi tugmalar orqali o'zingizga kerakli bo'limni tanlang.", disable_web_page_preview=True,
                         reply_markup=menu)

    await state.finish()
