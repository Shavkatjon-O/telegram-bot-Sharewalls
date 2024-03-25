from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router(name="start")


@router.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer("Hello, world!")
