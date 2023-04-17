import asyncio
import re
import sqlite3

import pandas as pd
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes, ChatActions
from aiogram.utils.exceptions import CantParseEntities

from data.config import ADMINS
from loader import dp, db, bot
from states.PersonalData import SendAds


@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.count_users()
    await bot.send_message(chat_id=message.chat.id, text=f"Userlarning umumiy soni: {users}")


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Reklama rasmi, videosi yoki audiosini matni bilan birga jo'nating!")

    await SendAds.photo.set()


@dp.message_handler(content_types=ContentTypes.ANY, user_id=ADMINS, state=SendAds.photo)
async def get_photo(message: types.Message, state: FSMContext):
    if message.photo:
        content_id = message.photo[-1].file_id
        file_caption = message.caption
        print(content_id)

    elif message.video:
        content_id = message.video.file_id
        file_caption = message.caption

    elif message.document:
        content_id = message.document.file_id
        file_caption = message.caption

    elif message.audio:
        content_id = message.audio.file_id
        file_caption = message.caption

    elif message.text:
        content_id = message.text
        file_caption = message.text
    else:
        await message.answer("Faqat audio, video, rasm, yoki tekst tashlang!")

    await state.update_data(
        {'content_id': content_id,
         'caption': file_caption}
    )

    data = await state.get_data()

    content_id = data.get('content_id')
    file_caption = data.get('caption')

    users = db.select_all_users()
    try:
        pass
    except CantParseEntities:
        await message.answer("Linkni to'g'ri shaklda jo'nating.")
    else:
        if message.photo:
            for user in users:
                user_id = user[0]
                await bot.send_photo(chat_id=user_id, photo=content_id, caption=file_caption, parse_mode="markdown")
                await asyncio.sleep(0.05)
                await state.finish()
        elif message.video:
            for user in users:
                user_id = user[0]
                await bot.send_video(chat_id=user_id, video=content_id, caption=file_caption, parse_mode="markdown")
                await asyncio.sleep(0.05)
                await state.finish()
        elif message.document:
            for user in users:
                user_id = user[0]
                await bot.send_document(chat_id=user_id, document=content_id, caption=file_caption,
                                        parse_mode="markdown")
                await asyncio.sleep(0.05)
                await state.finish()
        elif message.audio:
            for user in users:
                user_id = user[0]
                await bot.send_audio(chat_id=user_id, audio=content_id, caption=file_caption, parse_mode="markdown")
                await asyncio.sleep(0.05)
                await state.finish()
        elif message.text:
            for user in users:
                user_id = user[0]
                await bot.send_message(chat_id=user_id, text=message.text, parse_mode="markdown")
                await asyncio.sleep(0.05)
                await state.finish()


# @dp.message_handler(text="!cleandb", user_id=ADMINS)
# async def get_all_users(message: types.Message):
#     db.delete_users()
#     await message.answer("Baza tozalandi!")

@dp.message_handler(commands=['userlar'], user_id=ADMINS)
async def download_data(message: types.Message):
    # Send a "typing" action to the user to indicate that the bot is working
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)

    # Connect to the SQLite database
    conn = sqlite3.connect('data/main.db')

    # Query the data from the database
    query = 'SELECT * FROM Users'
    data = pd.read_sql_query(query, conn)

    # Save the data to an Excel file
    data.to_excel('my_data.xlsx', index=False)

    # Send the Excel file to the user as a document
    with open('my_data.xlsx', 'rb') as document:
        await bot.send_document(message.chat.id, document)

