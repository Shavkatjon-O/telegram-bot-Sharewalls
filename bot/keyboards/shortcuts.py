from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    """Creates row keyboard markup from given list of button texts."""

    buttons = [KeyboardButton(text=item) for item in items]
    reply_markup = ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True)

    return reply_markup
