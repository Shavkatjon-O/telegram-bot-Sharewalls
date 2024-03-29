from typing import Any

from aiogram.utils.i18n.middleware import I18nMiddleware
from aiogram.types import Message, CallbackQuery, InlineQuery

from asgiref.sync import sync_to_async
from bot.models import TelegramUser


class ACLMiddleware(I18nMiddleware):
    DEFAULT_LANGUAGE_CODE = "en"

    async def get_locale(
        self, message: Message | CallbackQuery | InlineQuery, data: dict[str, Any]
    ) -> str:

        if not message.from_user:
            return self.DEFAULT_LANGUAGE_CODE

        language_code: str | None = sync_to_async(TelegramUser.objects.get)(
            user_id=message.from_user.id
        )
        return language_code or self.DEFAULT_LANGUAGE_CODE
