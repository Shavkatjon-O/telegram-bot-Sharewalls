from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.enums import ContentType

from bot.filters.admin import AdminFilter
from bot.states import UploadStates
from bot.models import TelegramUser


router = Router(name="upload")


@router.message(Command("upload"), AdminFilter())
async def command_upload_handler(message: Message, current_user: TelegramUser, state: FSMContext) -> None:
    await state.set_state(UploadStates.UPLOAD_IMAGE)

    await message.answer("Send me an image")


@router.message(UploadStates.UPLOAD_IMAGE, F.content_type.in_([ContentType.PHOTO, ContentType.DOCUMENT]))
async def process_upload_image(
    message: Message, album: list[Message], current_user: TelegramUser, state: FSMContext
) -> None:

    await message.answer("Image received")
