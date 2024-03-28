from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, InputMediaPhoto, InputMediaDocument
from aiogram.fsm.context import FSMContext
from aiogram.enums import ContentType

from bot.filters.admin import AdminFilter
from bot.states import UploadStates
from bot.models import TelegramUser


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


router = Router(name="upload")
