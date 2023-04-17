# -*- coding: utf-8 -*-
import datetime

from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from json import dumps, loads, load
from data import config
from keyboards.inline.inline_phone import inline_english_test
from loader import dp, bot
from utils.db_api import level_db

questions = load(open("questions_new.json", "r", encoding="utf-8"))


def compose_markup(question: int):
    km = InlineKeyboardMarkup(row_width=4)
    for i in range(len(questions[question]["options"])):
        cd = {
            "question": question,
            "correct_answer": i
        }
        km.insert(InlineKeyboardButton(questions[question]["options"][i], callback_data=dumps(cd)))
    return km


def reset(uid: int):
    level_db.set_in_process(uid, False)
    level_db.change_questions_passed(uid, 0)
    level_db.change_questions_message(uid, 0)
    level_db.change_current_question(uid, 0)


@dp.callback_query_handler(lambda c: True)
async def answer_handler(callback: CallbackQuery):
    data = loads(callback.data)
    q = data["question"]
    is_correct = questions[q]["answer"] - 1 == data["correct_answer"]
    passed = level_db.get_questions_passed(callback.from_user.id)
    msg = level_db.get_questions_message(callback.from_user.id)
    if is_correct:
        passed += 1
        level_db.change_questions_passed(callback.from_user.id, passed)
    if q + 1 > len(questions) - 1:
        reset(callback.from_user.id)
        level_db.set_time_passed(callback.from_user.id, datetime.datetime.now())
        level_db.set_last_attempt(callback.from_user.id, passed)
        if passed >= 17:
            level = "Advanced"
        elif 14 <= passed < 17:
            level = "Upper-intermidiate"
        elif 11 <= passed < 14:
            level = "Intermidiate"
        elif 8 <= passed < 11:
            level = "Pre-intermidiate"
        elif 5 <= passed < 8:
            level = "Elementary"
        else:
            level = "Beginner"

        await bot.delete_message(callback.from_user.id, msg)
        await bot.send_message(
            callback.from_user.id,
            f"🎉 Test muvaffaqiyatli yakunlandi!\n\n"
            f"📊 To'g'ri javoblar soni: <u><b>{passed}</b></u>\n"
            f"📈 Hozirgi darajangiz: <u><b>{level}</b></u>\n"
            f"🔄 10 kundan keyin qayta test topshirishingiz mumkin!\n\n"
            f"<b>{level}</b> kursiga hoziroq ro'yxatdan o'tish uchun quyidagi tugmani bosing!",
            parse_mode="HTML", reply_markup=inline_english_test
        )
        return
    await bot.edit_message_text(
        questions[q + 1]["question"],
        callback.from_user.id,
        msg,
        reply_markup=compose_markup(q + 1),
        parse_mode="HTML"
    )


@dp.message_handler(commands=["play"])
async def go_handler(message: Message):
    if not level_db.is_exists(message.from_user.id):
        level_db.add(message.from_user.id)

    if level_db.get_last_attempt(message.from_user.id) != 0:
        last_attempt = level_db.get_last_attempt(message.from_user.id)
        date_passed = level_db.get_time_passed(message.from_user.id)
        date_now = datetime.datetime.now().date()
        date_delta = (date_now - date_passed.date()).days
        text_message = ""
        if date_delta < 10:
            if date_delta == 0:
                await message.answer(f"✅ Siz hozirgina test topshirdingiz!\n")
            else:
                text_message += f"✅ Siz {date_delta} kun oldin test topshirgansiz\n"
                text_message += f"📊 To'g'ri javoblar soni: <b>{last_attempt}</b>\n"
                text_message += f"🔄 Testni {date_passed.date() + datetime.timedelta(days=10)} sanada qayta topshira olasiz!"
                await message.answer(text_message)
    else:
        if level_db.is_in_process(message.from_user.id):
            await bot.send_message(message.from_user.id,
                                   "⚡️ Test davom etmoqda. Iltimos yakunlang!\n"
                                   "🚫 Bekor qilish uchun /finish ni bosing.",
                                   parse_mode="HTML")
            return
        level_db.set_in_process(message.from_user.id, True)
        msg = await bot.send_message(
            message.from_user.id,
            questions[0]["question"],
            reply_markup=compose_markup(0),
            parse_mode="HTML"
        )
        level_db.change_questions_message(message.from_user.id, msg.message_id)
        level_db.change_current_question(message.from_user.id, 0)
        level_db.change_questions_passed(message.from_user.id, 0)


@dp.message_handler(commands=["finish"])
async def quit_handler(message: Message):
    if not level_db.is_in_process(message.from_user.id):
        await bot.send_message(message.from_user.id, "❗️Hali testni boshlamadingiz.\n"
                                                     "💥 Testni boshlash uchun /play ni bosing.", parse_mode="HTML")
        return
    reset(message.from_user.id)
    await bot.send_message(message.from_user.id, "❌ Siz testni bekor qildingiz.\n"
                                                 "🔄 Qayta boshlash uchun /play ni bosing.",
                           parse_mode="HTML")


@dp.message_handler(text="📊 Darajani aniqlash testi")
async def start(message: Message):
    if not level_db.is_exists(message.from_user.id):
        level_db.add(message.from_user.id)
    if level_db.get_last_attempt(message.from_user.id) != 0:
        last_attempt = level_db.get_last_attempt(message.from_user.id)
        date_passed = level_db.get_time_passed(message.from_user.id)
        date_now = datetime.datetime.now().date()
        date_delta = (date_now - date_passed.date()).days

        if last_attempt >= 17:
            level = "Advanced"
        elif 14 <= last_attempt < 17:
            level = "Upper-intermidiate"
        elif 11 <= last_attempt < 14:
            level = "Intermidiate"
        elif 8 <= last_attempt < 11:
            level = "Pre-intermidiate"
        elif 5 <= last_attempt < 8:
            level = "Elementary"
        else:
            level = "Beginner"

        text_message = ""
        if date_delta < 10:
            if date_delta == 0:
                text_message += f"✅ Siz hozirgina test topshirdingiz!\n"
            else:
                text_message += f"✅ Siz {date_delta} kun oldin test topshirgansiz\n"
            text_message += f"📊 To'g'ri javoblar soni: <b>{last_attempt}</b>\n" \
                            f"📈 Avvalgi darajangiz: <u><b>{level}</b></u>\n"
            text_message += f"🔄 Testni {date_passed.date() + datetime.timedelta(days=10)} sanada qayta topshira olasiz!\n\n"
            text_message += f"<b>{level}</b> kursiga hoziroq ro'yxatdan o'tish uchun quyidagi tugmani bosing!"
        else:
            text_message += "⏱ Qayta test topshirish vaqti keldi!\n"
            text_message += f"📊 To'g'ri javoblar soni: <b>{last_attempt}</b>\n"\
                            f"📈 Avvalgi darajangiz: <u><b>{level}</b></u>\n"
            text_message += f"🔄 Testni qayta topshirish uchun /play ni bosing!\n\n"
            text_message += f"<b>{level}</b> kursiga hoziroq ro'yxatdan o'tish uchun quyidagi tugmani bosing!"
    else:
        text_message = "👋 Salom! \n🧠 Ingliz tilida qanday darajada ekanligingizni bilmoqchimisiz?.\n\n📝 Siz 20 ta " \
                       "savolga javob berishingiz kerak bo'ladi. \n⏱ Test taxminan 20 daqiqa davom etadi. " \
                       "\n\n<b>Testni boshlash</b> - /play\n<b>Testni tugatish</b> - /finish"

    await message.answer(text=text_message,
                         parse_mode="HTML", reply_markup=inline_english_test)
