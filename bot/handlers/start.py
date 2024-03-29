from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from django.utils.translation import gettext as _

from bot.models import TelegramUser


router = Router(name="start")


@router.message(CommandStart())
async def command_start_handler(message: Message, tg_user: TelegramUser) -> None:

    await message.answer(_("Hello, {first_name}!").format(first_name=tg_user.first_name))
