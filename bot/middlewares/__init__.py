from aiogram import Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware


def register_middlewares(dp: Dispatcher) -> None:
    from .auth import AuthMiddleware
    from .album import AlbumMiddleware

    dp.message.middleware(AuthMiddleware())
    dp.message.middleware(AlbumMiddleware())

    dp.callback_query.middleware(CallbackAnswerMiddleware())
