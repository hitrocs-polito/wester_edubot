from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default.branches_keyboard import branches
from keyboards.default.homepage_keyboard import menu
from loader import dp, bot


@dp.message_handler(text='⬅️Bosh sahifa')
async def homePage(message: types.Message):
    await message.answer("Bosh sahifa", reply_markup=menu)


@dp.message_handler(text="📍 Filiallarimiz")
async def send_branches(message: types.Message):
    await message.answer("Quyida barcha filiallarimiz haqida to'liq ma'lumot olishingiz mumkin!", reply_markup=branches)


@dp.message_handler(text="Eski shahar - 'Chinor'")
async def send_branches(message: types.Message):
    latitude = 40.7907341
    longitude = 72.3486376
    await message.answer("📍Manzil: Andijon shahar, Cho’lponshox ko’chasi, 26-uy"
                         "\n\n🔍️Mo'ljal: Andijon pochtasi"
                         "\n\n☎️  93-260-90-10\n📞  93-215-90-10")
    await bot.send_location(chat_id=message.chat.id, latitude=latitude, longitude=longitude)


@dp.message_handler(text="Eski shahar - 'O'zbegim'")
async def send_branches(message: types.Message):
    latitude = 40.787645
    longitude = 72.347520
    await message.answer("📍Manzil: Andijon shahar, Eski shahar hududi, Oltinko'l ko'cha. "
                         "\n\n🔍Mo‘ljal: O'zbegim savdo markazi qarshisida, Oila market 3-qavat."
                         "\n\n☎️  93-260-90-10\n📞  93-215-90-10")
    await bot.send_location(chat_id=message.chat.id, latitude=latitude, longitude=longitude)


@dp.message_handler(text="Yangi bozor - 'Leninskiy'")
async def send_branches(message: types.Message):
    latitude = 40.761958
    longitude = 72.353547
    await message.answer("📍Manzil:Andijon shahar, Milliy tiklanish ko'chasi"
                         "\n\n🔍️Mo'ljal: Malaka oshirish markazi yoni"
                         "\n\n☎️  93-260-90-10\n📞  93-215-90-10")
    await bot.send_location(chat_id=message.chat.id, latitude=latitude, longitude=longitude)


@dp.message_handler(text="Yangi bozor - 'Xolis'")
async def send_branches(message: types.Message):
    latitude = 40.756876
    longitude = 72.355529
    await message.answer("📍 Manzil: Andijon shahri, Yangi bozor, B.Rahimova koʻchasi"
                         "\n\n🔍 Moʻljal: Xolis savdomarkazi qarshisida"
                         "\n\n☎️  93-260-90-10\n📞  93-215-90-10")
    await bot.send_location(chat_id=message.chat.id, latitude=latitude, longitude=longitude)
