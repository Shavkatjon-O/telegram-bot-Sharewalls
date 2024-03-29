from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from django.utils.translation import gettext as _

from asgiref.sync import sync_to_async

from bot.models import TelegramUser
from bot.keyboards.shortcuts import make_row_keyboard


router = Router(name="language")


@router.message(Command("language"))
async def command_language_handler(message: Message, tg_user: TelegramUser) -> None:

    await message.answer(_("Choose your language"), reply_markup=make_row_keyboard(["ru", "uz"]))


@router.message(F.text.in_(["ru", "uz"]))
async def language_handler(message: Message, tg_user: TelegramUser) -> None:

    tg_user.language_code = message.text
    await sync_to_async(tg_user.save)()

    await message.answer(_("Language has been changed to {language}").format(language=message.text))
