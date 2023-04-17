from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🏢 Markaz haqida'),
            KeyboardButton(text='🎓 Kurslarimiz'),
        ],
        [
            KeyboardButton(text='📍 Filiallarimiz'),
            KeyboardButton(text='🏫 Prezident maktabi'),
        ],
        [
            KeyboardButton(text='📊 Darajani aniqlash testi'),
            KeyboardButton(text='📞 Mutaxassis bilan aloqa'),
        ],
    ],
    resize_keyboard=True
)
