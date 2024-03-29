from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from bot.models import TelegramUser
from bot.filters.admin import AdminFilter
from bot.states.upload import UploadStates


router = Router(name="upload")


@router.message(Command(commands=["upload"]), AdminFilter())
async def command_upload_handler(message: Message, tg_user: TelegramUser, state: FSMContext) -> None:
    """Handler for uploading images to database by admin users only."""

    await state.set_state(UploadStates.UPLOAD_IMAGE)
