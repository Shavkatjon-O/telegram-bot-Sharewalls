from aiogram import Router


def get_handlers_router() -> Router:
    from . import start, upload

    router = Router()
    router.include_router(start.router)
    router.include_router(upload.router)

    return router
