import asyncio

from typing import Any, Callable, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message


class AlbumMiddleware(BaseMiddleware):
    album_data: dict = {}

    def __init__(self, latency: Union[int, float] = 0.01):
        self.latency = latency

    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        message: Message,
        data: dict[str, Any],
    ) -> Any:

        if not isinstance(message, Message):
            return await handler(message, data)

        if not message.from_user:
            return await handler(message, data)

        if not message.media_group_id and (message.document or message.photo):
            data["album"] = [message]
            return await handler(message, data)

        if not message.media_group_id:
            return await handler(message, data)

        try:
            self.album_data[message.media_group_id].append(message)
        except KeyError:
            self.album_data[message.media_group_id] = [message]
            await asyncio.sleep(self.latency)

            data["is_last"] = True
            data["album"] = self.album_data[message.media_group_id]

            await handler(message, data)

        if message.media_group_id and data.get("is_last"):
            del self.album_data[message.media_group_id]
            del data["is_last"]
