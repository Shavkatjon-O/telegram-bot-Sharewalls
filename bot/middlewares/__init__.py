from aiogram import Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

from bot.core.loader import i18n as _i18n


def register_middlewares(dp: Dispatcher) -> None:

    from .auth import AuthMiddleware
    from .album import AlbumMiddleware
    from .i18n import ACLMiddleware

    dp.message.middleware(AuthMiddleware())
    dp.message.middleware(AlbumMiddleware())

    dp.message.middleware(ACLMiddleware(i18n=_i18n))
    dp.callback_query.middleware(ACLMiddleware(i18n=_i18n))
    dp.inline_query.middleware(ACLMiddleware(i18n=_i18n))

    dp.callback_query.middleware(CallbackAnswerMiddleware())
