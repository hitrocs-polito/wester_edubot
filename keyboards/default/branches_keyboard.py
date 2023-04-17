from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

branches = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Eski shahar - 'Chinor'"),
            KeyboardButton(text="Yangi bozor - 'Leninskiy'"),
        ],
        [
            KeyboardButton(text="Eski shahar - 'O'zbegim'"),
            KeyboardButton(text="Yangi bozor - 'Xolis'"),
        ],
        [
            KeyboardButton(text="⬅️Bosh sahifa"),
        ],
    ],
    resize_keyboard=True
)
