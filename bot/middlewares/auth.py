from typing import Any, Callable, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from asgiref.sync import sync_to_async
from django.utils.translation import activate
from bot.models import TelegramUser

from loguru import logger


class AuthMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        message: Message,
        data: dict[str, Any],
    ) -> Any:

        user = message.from_user

        if not isinstance(message, Message):
            return await handler(message, data)
        if not user:
            return await handler(message, data)

        try:
            tg_user = await sync_to_async(TelegramUser.objects.get)(user_id=user.id)

            if tg_user.language_code:
                activate(tg_user.language_code)

        except TelegramUser.DoesNotExist:
            tg_user = await sync_to_async(TelegramUser.objects.create)(
                user_id=user.id,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name,
            )
            logger.info(f"New User - {tg_user.user_id} - {tg_user.username}")

        data["tg_user"] = tg_user
        return await handler(message, data)
