from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

contact_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="📞 Kontaktni ulashish", request_contact=True),
        ],
    ],
    resize_keyboard=True
)