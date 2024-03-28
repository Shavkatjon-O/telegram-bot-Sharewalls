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
    UploadStates.UPLOAD_IMAGE, F.content_type.in_([ContentType.DOCUMENT, ContentType.PHOTO])
)
async def process_upload_image(
    message: Message, media_events: list[Message], current_user: TelegramUser, state: FSMContext
):
    """Handler for processing image for upload that is sent as MediaGroup, Document, or Photo"""

    media_group = []
    for _message in media_events:
        if _message.photo:
            media_group.append(InputMediaPhoto(media=_message.photo[-1].file_id))
        else:
            media_group.append(InputMediaDocument(media=_message.document.file_id))

    await message.answer_media_group(media_group)
