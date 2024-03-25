import uvloop
from loguru import logger

from bot.handlers import get_handlers_router
from bot.core.loader import bot, dp


async def on_startup() -> None:
    logger.info("Bot Starting ...")

    dp.include_router(get_handlers_router())

    bot_info = await bot.get_me()

    logger.info(f"Name     - {bot_info.full_name}")
    logger.info(f"Username - @{bot_info.username}")
    logger.info(f"ID       - {bot_info.id}")

    states: dict[bool | None, str] = {
        True: "Enabled",
        False: "Disabled",
        None: "Unknown (This's not a bot)",
    }

    logger.info(f"Groups Mode  - {states[bot_info.can_join_groups]}")
    logger.info(f"Privacy Mode - {states[not bot_info.can_read_all_group_messages]}")
    logger.info(f"Inline Mode  - {states[bot_info.supports_inline_queries]}")

    logger.info("Bot Started")


async def on_shutdown() -> None:
    logger.info("Bot Stopping ...")

    await dp.storage.close()
    await dp.fsm.storage.close()

    await bot.delete_webhook()
    await bot.session.close()

    logger.info("Bot Stopped")


async def main() -> None:
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    uvloop.run(main())
