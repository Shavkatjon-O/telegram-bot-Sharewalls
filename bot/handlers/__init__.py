from aiogram import Router


def get_handlers_router() -> Router:
    from . import start, upload, language

    router = Router()
    router.include_router(start.router)
    router.include_router(upload.router)
    router.include_router(language.router)

    return router
