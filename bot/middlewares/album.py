from typing import Any, Callable, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message
import asyncio


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

        if not message.media_group_id:
            return await handler(message, data)

        try:
            self.album_data[message.media_group_id].append(message)
        except KeyError:
            self.album_data[message.media_group_id] = [message]
            await asyncio.sleep(self.latency)

            data["_is_last"] = True
            data["album"] = self.album_data[message.media_group_id]

        if message.media_group_id and data.get("_is_last"):
            del self.album_data[message.media_group_id]
            del data["_is_last"]

        return await handler(message, data)
