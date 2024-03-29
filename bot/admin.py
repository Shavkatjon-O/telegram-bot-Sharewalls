from django.contrib import admin
from bot import models


admin.site.register(models.Wallpaper)
admin.site.register(models.WallpaperImage)
admin.site.register(models.TelegramAdmin)
admin.site.register(models.TelegramUser)
