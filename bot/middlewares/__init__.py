from aiogram import Dispatcher


def register_middlewares(dp: Dispatcher) -> None:
    from .auth import AuthMiddleware
    from .media_group import MediaGroupMiddleware

    dp.message.middleware(AuthMiddleware())
    dp.message.middleware(MediaGroupMiddleware())
