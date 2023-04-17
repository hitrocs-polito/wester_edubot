import sqlite3

from aiogram import types
from aiogram.types import CallbackQuery

from data.config import ADMINS
from keyboards.default.courses_keyboard import courses, courses_dasturlash, courses_english
from keyboards.default.homepage_keyboard import menu
from keyboards.inline.inline_phone import inline_backend, inline_front, inline_foundation, inline_savodxonlik, \
    inline_ielts, inline_cefr, inline_general, inline_pm, inline_dizayn
from loader import dp, db, bot
from utils.db_api import level_db


@dp.message_handler(text="🏢 Markaz haqida")
async def bot_start(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="AgACAgIAAxkBAAII1mQ8ZvLpB6UQwYg38Tvqvfll8TiKAAL3xDEbct95S5ugDZpnzXpFAQADAgADeQADLwQ",
                         caption=
                         "Biz boshladik! 😊 \n\nAzizlar kelajak tomon yana bir ulkan qadam qoʻyildi!\n\n"
                         "🚀 WESTER IT Academy — IT olamidagi sizning koʻmakdoshingizdir! Raqamli dunyoda kelajak kasblarini soha ekspertlari va eng soʻnggi texnologiyalar bilan oʻrganing.\n\n"
                         "✅ Bizning yuqori malakali mutaxassislarimiz IT koʻnikmalaringizni shakllantirish va qobiliyatlaringizni rivojlantirishga yaqindan yordam beradi. IT olamidagi karyerangiz biz bilan yana-da yaqinroq boʻladi!\n\n"
                         "💡 Ishonchimiz komilki WESTER IT Academy orzular amalga oshuvchi, yangi gʻoyalarni yaratuvchi va IT yoʻnalishidagi insonlar orzusidagi makondir!")


@dp.message_handler(text="🎓 Kurslarimiz")
async def bot_start(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="AgACAgIAAxkBAAII5GQ8Z38s-0FUOzvuxqNKHCODFbJkAAKsxDEbFhSISynLLHpemVxKAQADAgADeQADLwQ",
                         caption=
                         "«Wester | School» da asosiy 4 ta kurs yo'nalishi bor:\n\n"
                         "1. <b>Ingliz tili</b>\n"
                         "2. <b>Dasturlash</b>\n"
                         "3. <b>Dizayn</b>\n\n"
                         "Yo'nalishlarda mavjud kurslarni ko'rish uchun quyidagi bo'limlardan birini tanlang.",
                         reply_markup=courses)


@dp.message_handler(text="Dasturlash")
async def bot_start(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="AgACAgIAAxkBAAII62Q8Z-g2jzy6PtULCnutc4owDFdMAAKtxDEbFhSIS2eVVO7wlXpRAQADAgADeQADLwQ",
                         caption=
                         "Dasturlash yo'nalishida mavjud kurslarimiz:\n\n"
                         "1. <b>Frontend</b>\n"
                         "2. <b>Backend</b>\n"
                         "3. <b>Kompyuter savodxonligi</b>\n"
                         "4. <b>IT foundation</b>\n\n"
                         "Kurslar haqidamalumot olish uchun quyidagi bo'limlardan birini tanlang.",
                         reply_markup=courses_dasturlash)


@dp.message_handler(text="Backend")
async def bot_start(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="AgACAgIAAxkBAAII-mQ8aAcNN3y5YQinBVJbxqJDHl9sAAKvxDEbFhSISyNfgqwWtftxAQADAgADeQADLwQ",
                         caption=
                         "✅ Siz ham o'rgana olasiz!\n\nZamon texnologiyalar bilan rivojlanib borayabdi. Shunday davrda ulardan qanday "
                         "foydalanishni bilmasangiz o'z ish o'rningizni boshqalarga bo'shatishingizga to'g'ri keladi.\n\n🔝 Sohangizda "
                         "yanada yuksalishingizga yordam beruvchi WESTER IT Academyning 'Kompyuter "
                         "savodxonligi' kursi aynan siz uchun.\n\n💡Kurs davomiyligi 2 oy bo'lib o'zingizga qulay vaqtni tanlashinigiz "
                         "mumkin.\n\nKurs davomida quyidagilarni o'rganasiz: Word, Excel, PowerPoint va bonus tariqasida WINDOWS(sistema) "
                         "bosish bilimlariga ega bo'lasiz.", reply_markup=inline_backend)


@dp.message_handler(text="Front-end")
async def bot_start(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="AgACAgIAAxkBAAII8mQ8Z_qJwqWmd0nPvqWJxGO6WDCSAAKuxDEbFhSISz0gCBhr6NFbAQADAgADeQADLwQ",
                         caption=
                         "✅ Siz ham o'rgana olasiz!\n\nZamon texnologiyalar bilan rivojlanib borayabdi. Shunday davrda ulardan qanday "
                         "foydalanishni bilmasangiz o'z ish o'rningizni boshqalarga bo'shatishingizga to'g'ri keladi.\n\n🔝 Sohangizda "
                         "yanada yuksalishingizga yordam beruvchi WESTER IT Academyning 'Kompyuter "
                         "savodxonligi' kursi aynan siz uchun.\n\n💡Kurs davomiyligi 2 oy bo'lib o'zingizga qulay vaqtni tanlashinigiz "
                         "mumkin.\n\nKurs davomida quyidagilarni o'rganasiz: Word, Excel, PowerPoint va bonus tariqasida WINDOWS(sistema) "
                         "bosish bilimlariga ega bo'lasiz.", reply_markup=inline_front)


@dp.message_handler(text="IT foundation")
async def bot_start(message: types.Message):
    await message.answer(
        "✅ Siz ham o'rgana olasiz!\n\nZamon texnologiyalar bilan rivojlanib borayabdi. Shunday davrda ulardan qanday "
        "foydalanishni bilmasangiz o'z ish o'rningizni boshqalarga bo'shatishingizga to'g'ri keladi.\n\n🔝 Sohangizda "
        "yanada yuksalishingizga yordam beruvchi WESTER IT Academyning 'Kompyuter "
        "savodxonligi' kursi aynan siz uchun.\n\n💡Kurs davomiyligi 2 oy bo'lib o'zingizga qulay vaqtni tanlashinigiz "
        "mumkin.\n\nKurs davomida quyidagilarni o'rganasiz: Word, Excel, PowerPoint va bonus tariqasida WINDOWS(sistema) "
        "bosish bilimlariga ega bo'lasiz.", reply_markup=inline_foundation)


@dp.message_handler(text="Kompyuter savodxonligi")
async def bot_start(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="AgACAgIAAxkBAAIJCGQ8aB7Roh5j3QEHpuACOF-HMWRGAAKxxDEbFhSIS5Z5BXr36kmzAQADAgADeQADLwQ",
                         caption=
                         "✅ Siz ham o'rgana olasiz!\n\nZamon texnologiyalar bilan rivojlanib borayabdi. Shunday davrda ulardan qanday "
                         "foydalanishni bilmasangiz o'z ish o'rningizni boshqalarga bo'shatishingizga to'g'ri keladi.\n\n🔝 Sohangizda "
                         "yanada yuksalishingizga yordam beruvchi WESTER IT Academyning 'Kompyuter "
                         "savodxonligi' kursi aynan siz uchun.\n\n💡Kurs davomiyligi 2 oy bo'lib o'zingizga qulay vaqtni tanlashinigiz "
                         "mumkin.\n\nKurs davomida quyidagilarni o'rganasiz: Word, Excel, PowerPoint va bonus tariqasida WINDOWS(sistema) "
                         "bosish bilimlariga ega bo'lasiz.", reply_markup=inline_savodxonlik)


@dp.callback_query_handler(text='frontend')
async def backend_true(call: CallbackQuery):
    await call.message.answer("✅ Qabul qilindi.\n\nMutaxassislarimiz tez orada siz bilan bog'lanishadi.",
                              reply_markup=menu)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"#registration\n"
                                f"Foydalanuvchi:\n\n"
                                f"Ismi: {db.get_firstname(call.from_user.id)[0]}\n"
                                f"Familiya: {db.get_lastname(call.from_user.id)[0]}\n"
                                f"Nomeri: {db.get_number(call.from_user.id)[0]}\n"
                                f"Kurs nomi: Frontend")
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='foundation')
async def backend_true(call: CallbackQuery):
    await call.message.answer("✅ Qabul qilindi.\n\nMutaxassislarimiz tez orada siz bilan bog'lanishadi.",
                              reply_markup=menu)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"#registration\n"
                                f"Foydalanuvchi:\n\n"
                                f"Ismi: {db.get_firstname(call.from_user.id)[0]}\n"
                                f"Familiya: {db.get_lastname(call.from_user.id)[0]}\n"
                                f"Nomeri: {db.get_number(call.from_user.id)[0]}\n"
                                f"Kurs nomi: Foundation")
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='savodxonlik')
async def backend_true(call: CallbackQuery):
    await call.message.answer("✅ Qabul qilindi.\n\nMutaxassislarimiz tez orada siz bilan bog'lanishadi.",
                              reply_markup=menu)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"#registration\n"
                                f"Foydalanuvchi:\n\n"
                                f"Ismi: {db.get_firstname(call.from_user.id)[0]}\n"
                                f"Familiya: {db.get_lastname(call.from_user.id)[0]}\n"
                                f"Nomeri: {db.get_number(call.from_user.id)[0]}\n"
                                f"Kurs nomi: Kompyuter savodxonlik")
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='backend')
async def backend_true(call: CallbackQuery):
    await call.message.answer("✅ Qabul qilindi.\n\nMutaxassislarimiz tez orada siz bilan bog'lanishadi.",
                              reply_markup=menu)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"#registration\n"
                                f"Foydalanuvchi:\n\n"
                                f"Ismi: {db.get_firstname(call.from_user.id)[0]}\n"
                                f"Familiya: {db.get_lastname(call.from_user.id)[0]}\n"
                                f"Nomeri: {db.get_number(call.from_user.id)[0]}\n"
                                f"Kurs nomi: Backend django")
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.message_handler(text="Ingliz tili")
async def bot_start(message: types.Message):
    await message.answer(
        "Ingliz tili yo'nalishida mavjud kurslarimiz:\n\n"
        "1. <b>General English</b>\n"
        "2. <b>IELTS</b>\n"
        "3. <b>CEFR</b>\n"
        "Kurslar haqidamalumot olish uchun quyidagi bo'limlardan birini tanlang.", reply_markup=courses_english)


@dp.message_handler(text="IELTS")
async def bot_start(message: types.Message):
    await message.answer(
        "🔥 2 oyda CEFR B2 \n\nWESTER School o'quvchisi 🎓 Abduhamidov Ahrorbek CEFR bo’yicha C1 ga 2 ball yetmasdan B2 natijaga erishdilar. \n\n"
        "🏻‍🏫 Teacher: Ms Zebo\n\nO’quvchilarimizga kelgusi ishlarida ulkan muvaffaqiyatlar va omadlar tilab qolamiz. \n\n"
        "📈Siz ham CEFR bilan bu yil talaba boʻlishni yoki ish joyingizda o'sishni istasangiz yangi 6 oyga moʻljallangan CEFR 1.0  guruhlariga qoʻshiling.",
        reply_markup=inline_ielts)


@dp.message_handler(text="General English")
async def bot_start(message: types.Message):
    await message.answer(
        "🔥 2 oyda CEFR B2 \n\nWESTER School o'quvchisi 🎓 Abduhamidov Ahrorbek CEFR bo’yicha C1 ga 2 ball yetmasdan B2 natijaga erishdilar. \n\n"
        "🏻‍🏫 Teacher: Ms Zebo\n\nO’quvchilarimizga kelgusi ishlarida ulkan muvaffaqiyatlar va omadlar tilab qolamiz. \n\n"
        "📈Siz ham CEFR bilan bu yil talaba boʻlishni yoki ish joyingizda o'sishni istasangiz yangi 6 oyga moʻljallangan CEFR 1.0  guruhlariga qoʻshiling.",
        reply_markup=inline_general)


@dp.message_handler(text="CEFR")
async def bot_start(message: types.Message):
    await message.answer(
        "🔥 2 oyda CEFR B2 \n\nWESTER School o'quvchisi 🎓 Abduhamidov Ahrorbek CEFR bo’yicha C1 ga 2 ball yetmasdan B2 natijaga erishdilar. \n\n"
        "🏻‍🏫 Teacher: Ms Zebo\n\nO’quvchilarimizga kelgusi ishlarida ulkan muvaffaqiyatlar va omadlar tilab qolamiz. \n\n"
        "📈Siz ham CEFR bilan bu yil talaba boʻlishni yoki ish joyingizda o'sishni istasangiz yangi 6 oyga moʻljallangan CEFR 1.0  guruhlariga qoʻshiling.",
        reply_markup=inline_cefr)


@dp.callback_query_handler(text='ielts')
async def backend_true(call: CallbackQuery):
    await call.message.answer("✅ Qabul qilindi.\n\nMutaxassislarimiz tez orada siz bilan bog'lanishadi.",
                              reply_markup=menu)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"#registration\n"
                                f"Foydalanuvchi:\n\n"
                                f"Ismi: {db.get_firstname(call.from_user.id)[0]}\n"
                                f"Familiya: {db.get_lastname(call.from_user.id)[0]}\n"
                                f"Nomeri: {db.get_number(call.from_user.id)[0]}\n"
                                f"Kurs nomi: IELTS")
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='cefr')
async def backend_true(call: CallbackQuery):
    await call.message.answer("✅ Qabul qilindi.\n\nMutaxassislarimiz tez orada siz bilan bog'lanishadi.",
                              reply_markup=menu)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"#registration\n"
                                f"Foydalanuvchi:\n\n"
                                f"Ismi: {db.get_firstname(call.from_user.id)[0]}\n"
                                f"Familiya: {db.get_lastname(call.from_user.id)[0]}\n"
                                f"Nomeri: {db.get_number(call.from_user.id)[0]}\n"
                                f"Kurs nomi: CEFR")
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='general')
async def backend_true(call: CallbackQuery):
    await call.message.answer("✅ Qabul qilindi.\n\nMutaxassislarimiz tez orada siz bilan bog'lanishadi.",
                              reply_markup=menu)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"#registration\n"
                                f"Foydalanuvchi:\n\n"
                                f"Ismi: {db.get_firstname(call.from_user.id)[0]}\n"
                                f"Familiya: {db.get_lastname(call.from_user.id)[0]}\n"
                                f"Nomeri: {db.get_number(call.from_user.id)[0]}\n"
                                f"Kurs nomi: General English")
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.message_handler(text="Grafik dizayn")
async def bot_start(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="AgACAgIAAxkBAAIJAWQ8aBaIqeJjDjRS_7fpgi6brw1qAAKwxDEbFhSIS5Nzq_3n4JZGAQADAgADeQADLwQ",
                         caption=
                         "✅ Siz ham o'rgana olasiz!\n\nZamon texnologiyalar bilan rivojlanib borayabdi. Shunday davrda ulardan qanday "
                         "foydalanishni bilmasangiz o'z ish o'rningizni boshqalarga bo'shatishingizga to'g'ri keladi.\n\n🔝 Sohangizda "
                         "yanada yuksalishingizga yordam beruvchi WESTER IT Academyning 'Kompyuter "
                         "savodxonligi' kursi aynan siz uchun.\n\n💡Kurs davomiyligi 2 oy bo'lib o'zingizga qulay vaqtni tanlashinigiz "
                         "mumkin.\n\nKurs davomida quyidagilarni o'rganasiz: Word, Excel, PowerPoint va bonus tariqasida WINDOWS(sistema) "
                         "bosish bilimlariga ega bo'lasiz.",
                         reply_markup=inline_dizayn)


@dp.callback_query_handler(text='dizayn')
async def backend_true(call: CallbackQuery):
    await call.message.answer("✅ Qabul qilindi.\n\nMutaxassislarimiz tez orada siz bilan bog'lanishadi.",
                              reply_markup=menu)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"#registration\n"
                                f"Foydalanuvchi:\n\n"
                                f"Ismi: {db.get_firstname(call.from_user.id)[0]}\n"
                                f"Familiya: {db.get_lastname(call.from_user.id)[0]}\n"
                                f"Nomeri: {db.get_number(call.from_user.id)[0]}\n"
                                f"Kurs nomi: Grafik dizayn")
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='english_test')
async def backend_true(call: CallbackQuery):
    await call.message.answer("✅ Qabul qilindi.\n\nMutaxassislarimiz tez orada siz bilan bog'lanishadi.",
                              reply_markup=menu)
    passed = level_db.get_last_attempt(call.from_user.id)
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
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"#registration_from_test\n"
                                f"Foydalanuvchi:\n\n"
                                f"Ismi: {db.get_firstname(call.from_user.id)[0]}\n"
                                f"Familiya: {db.get_lastname(call.from_user.id)[0]}\n"
                                f"Nomeri: {db.get_number(call.from_user.id)[0]}\n"
                                f"Test darajasi: <b>{level}</b>\n"
                                f"Kurs nomi: {level} Ingliz tili")
    await call.message.delete()
    await call.answer(cache_time=60)
