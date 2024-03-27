from core.settings.base import *

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PASS"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.str("DB_PORT"),
    }
}

CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ("https://fwallsbot.dev-space.uz",)

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]
