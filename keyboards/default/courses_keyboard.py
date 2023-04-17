from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

courses = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ingliz tili"),
            KeyboardButton(text="Dasturlash"),
        ],
        [
            KeyboardButton(text="Grafik dizayn"),
            KeyboardButton(text="⬅️Bosh sahifa"),
        ],
    ],
    resize_keyboard=True
)

courses_dasturlash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="IT foundation"),
            KeyboardButton(text="Front-end"),
        ],
        [
            KeyboardButton(text="Backend"),
            KeyboardButton(text="Kompyuter savodxonligi"),
        ],
        [
            KeyboardButton(text="⬅️Bosh sahifa"),
        ],
    ],
    resize_keyboard=True
)
courses_english = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="General English"),
        ],
        [
            KeyboardButton(text="IELTS"),
            KeyboardButton(text="CEFR"),
        ],
        [
            KeyboardButton(text="⬅️Bosh sahifa"),
        ],
    ],
    resize_keyboard=True
)
