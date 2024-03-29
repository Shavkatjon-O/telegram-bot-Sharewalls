from aiogram import Router, F
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.models import TelegramUser
from bot.filters.admin import AdminFilter
from bot.states.admin import UploadStates
from bot.keyboards import inline, reply


router = Router(name="upload")


@router.message(Command(commands=["upload"]), AdminFilter())
async def command_upload_handler(
    message: Message, tg_user: TelegramUser, state: FSMContext
) -> None:
    """Handler for uploading images to database by admin users only."""

    await state.set_state(UploadStates.UPLOAD_IMAGE)


@router.message(
    UploadStates.UPLOAD_IMAGE, F.content_type.in_([ContentType.PHOTO, ContentType.DOCUMENT])
)
async def process_image(
    message: Message, album: list[Message], tg_user: TelegramUser, state: FSMContext
) -> None:
    """Handler for uploading images to database by admin users only."""

    await state.set_state(UploadStates.CONFIRMATION)


@router.message(UploadStates.CONFIRMATION, F.text == reply.ConfirmUploadChoices.ADD_IMAGE)
async def process_add_image(
    message: Message, album: list[Message], tg_user: TelegramUser, state: FSMContext
) -> None:

    await state.set_state(UploadStates.UPLOAD_IMAGE)


@router.message(UploadStates.CONFIRMATION, F.text == reply.ConfirmUploadChoices.FINISH)
async def process_finish(
    message: Message, album: list[Message], tg_user: TelegramUser, state: FSMContext
) -> None:
    pass


@router.message(UploadStates.CONFIRMATION, F.text == reply.ConfirmUploadChoices.CANCEL)
async def process_cancel(
    message: Message, album: list[Message], tg_user: TelegramUser, state: FSMContext
) -> None:
    pass
