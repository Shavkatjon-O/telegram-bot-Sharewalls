from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router(name="upload")


@router.message(Command(commands=["upload"]))
async def command_upload_handler(message: Message) -> None:

    await message.answer("Uploading file...")
