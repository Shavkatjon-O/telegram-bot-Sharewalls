from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


confirm_upload = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Upload different one"),
        ],
        [
            KeyboardButton(text="Upload"),
            KeyboardButton(text="Cancel"),
        ],
    ],
    resize_keyboard=True,
)
