from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class ConfirmUploadChoices:
    ADD_IMAGE = "Отправить фото"
    FINISH = "✅ Загрузить"
    CANCEL = "❌ Отмена"


confirm_upload = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=ConfirmUploadChoices.UPLOAD_IMAGE)],
        [KeyboardButton(text=ConfirmUploadChoices.FINISH), KeyboardButton(text=ConfirmUploadChoices.CANCEL)],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
