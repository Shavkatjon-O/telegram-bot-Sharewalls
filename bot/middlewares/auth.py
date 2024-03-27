from __future__ import annotations

from aiogram import BaseMiddleware
from aiogram.types import Message

from asgiref.sync import sync_to_async

from bot.models import TelegramUser

from loguru import logger

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable, Awaitable


class AuthMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any],
    ) -> Any:

        message: Message = event
        user = message.from_user

        if not isinstance(event, Message):
            return await handler(event, data)
        if not user:
            return await handler(event, data)

        try:
            current_user = await sync_to_async(TelegramUser.objects.get)(user_id=user.id)
        except TelegramUser.DoesNotExist:
            current_user = await sync_to_async(TelegramUser.objects.create)(
                user_id=user.id,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name,
            )
            logger.info(f"New User - {current_user.user_id} - {current_user.username}")

        data["current_user"] = current_user
        return await handler(event, data)
