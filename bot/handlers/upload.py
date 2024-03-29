from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, InputMediaDocument, InputMediaPhoto
from aiogram.fsm.context import FSMContext
from aiogram.enums import ContentType

from bot.models import TelegramUser
from bot.filters.admin import AdminFilter
from bot.keyboards import inline, reply
from bot.states import UploadStates


router = Router(name="upload")


@router.message(Command("upload"), AdminFilter())
async def upload_command_handler(message: Message, current_user: TelegramUser, state: FSMContext) -> None:

    await state.set_state(UploadStates.UPLOAD_IMAGE)
    await message.answer("Send an image.")


@router.message(UploadStates.UPLOAD_IMAGE, F.content_type.in_([ContentType.DOCUMENT, ContentType.PHOTO]))
async def process_upload_image(
    message: Message, media_events: list[Message], current_user: TelegramUser, state: FSMContext
) -> None:
    """Handler for processing upload image that is sent as MediaGroup, Document, or Photo"""

    await state.set_state(UploadStates.CONFIRMATION)

    media_group = []
    for _message in media_events:
        if _message.photo:
            media_group.append(InputMediaPhoto(media=_message.photo[-1].file_id))
        else:
            media_group.append(InputMediaDocument(media=_message.document.file_id))

    await message.answer_media_group(media_group)
    await message.answer("Saved ✅", reply_markup=reply.confirm_upload)


@router.message(UploadStates.CONFIRMATION, F.text == reply.ConfirmUploadChoices.UPLOAD_IMAGE)
async def process_confirm_upload(message: Message, current_user: TelegramUser, state: FSMContext) -> None:

    await state.set_state(UploadStates.UPLOAD_IMAGE)
    await message.answer("Send an image.")


@router.message(UploadStates.CONFIRMATION, F.text == reply.ConfirmUploadChoices.FINISH)
async def process_finish_upload(message: Message, current_user: TelegramUser, state: FSMContext) -> None:
    pass


@router.message(UploadStates.CONFIRMATION, F.text == reply.ConfirmUploadChoices.CANCEL)
async def process_cancel_upload(message: Message, current_user: TelegramUser, state: FSMContext) -> None:
    pass
