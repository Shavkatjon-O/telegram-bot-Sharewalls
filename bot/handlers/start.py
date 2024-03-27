from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.models import TelegramUser


router = Router(name="start")


@router.message(CommandStart())
async def command_start_handler(message: Message, current_user: TelegramUser) -> None:

    await message.answer(f"Hello, {current_user.first_name}!")
