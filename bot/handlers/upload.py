from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, InputMediaDocument, InputMediaPhoto
from aiogram.fsm.context import FSMContext
from aiogram.enums import ContentType

from bot.filters.admin import AdminFilter
from bot.states import UploadStates
from bot.models import TelegramUser


router = Router(name="upload")


"""

1. User sends /upload command
2. Bot asks user to send an image
3. User sends an image
4. Bot sends the image to user and asks for confirmation
5. User sends confirmation
6. Bot asks to add another one or finish
7. User sends another one or finish
8. User sends /finish command
9. Bot saves images to database

"""


@router.message(Command("upload"), AdminFilter())
async def upload_command_handler(message: Message, current_user: TelegramUser, state: FSMContext):

    await state.set_state(UploadStates.UPLOAD_IMAGE)
    await message.answer("Send an image.")


@router.message(
    UploadStates.UPLOAD_IMAGE,
    F.content_type == ContentType.DOCUMENT or F.content_type == ContentType.PHOTO,
    F.media_group_id,
)
async def process_upload_image(
    message: Message, album_message: list[Message], current_user: TelegramUser, state: FSMContext
):
    media_group = []
    for _message in album_message:
        if _message.photo:
            media_group.append(InputMediaPhoto(media=_message.photo[-1].file_id))
        else:
            media_group.append(InputMediaDocument(media=_message.document.file_id))

    await message.answer_media_group(media_group)
    await message.answer("Do you want to add another one or finish?")
