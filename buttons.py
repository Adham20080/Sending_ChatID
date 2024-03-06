from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn = [
    [KeyboardButton(text="Chat users"), KeyboardButton(text="All users")]
]
keyboard = ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True)
