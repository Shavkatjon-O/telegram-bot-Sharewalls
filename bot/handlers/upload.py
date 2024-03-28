from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, InputMediaDocument, InputMediaPhoto
from aiogram.fsm.context import FSMContext
from aiogram.enums import ContentType

from bot.models import TelegramUser
from bot.filters.admin import AdminFilter
from bot.keyboards.reply.upload import confirm_upload
from bot.states import UploadStates


router = Router(name="upload")


@router.message(Command("upload"), AdminFilter())
async def upload_command_handler(message: Message, current_user: TelegramUser, state: FSMContext):

    await state.set_state(UploadStates.UPLOAD_IMAGE)
    await message.answer("Send an image.")


@router.message(
    UploadStates.UPLOAD_IMAGE,
    F.content_type.in_([ContentType.DOCUMENT, ContentType.PHOTO]),
    F.media_group_id,
)
async def process_upload_image_group(
    message: Message, album_message: list[Message], current_user: TelegramUser, state: FSMContext
):
    """Handler for processing image for upload that is sent as a MediaGroup."""

    media_group = []
    for _message in album_message:
        if _message.photo:
            media_group.append(InputMediaPhoto(media=_message.photo[-1].file_id))
        else:
            media_group.append(InputMediaDocument(media=_message.document.file_id))

    await message.answer_media_group(media_group)


@router.message(
    UploadStates.UPLOAD_IMAGE,
    F.content_type.in_([ContentType.DOCUMENT, ContentType.PHOTO]),
    F.media_group_id.is_(None),
)
async def process_upload_image(message: Message, current_user: TelegramUser, state: FSMContext):
    """Handler for processing image for upload that is send as a single document or photo."""

    await message.answer("Image is received!")
