from aiogram import Dispatcher


def register_middlewares(dp: Dispatcher) -> None:
    from .auth import AuthMiddleware

    dp.message.middleware(AuthMiddleware())
