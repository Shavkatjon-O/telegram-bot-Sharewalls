from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from aiogram.utils.i18n.core import I18n

from django.conf import settings

token = settings.TELEGRAM_BOT_TOKEN

bot = Bot(token=token, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

i18n: I18n = I18n(path=settings.BASE_DIR / "locales", default_locale="en", domain="django")
