from django.contrib import admin
from . import models

admin.site.register(models.FileMessage)
admin.site.register(models.MediaGroupItem)
admin.site.register(models.Admin)
admin.site.register(models.TGusers)

admin.site.register(models.Wallpaper)
admin.site.register(models.WallpaperImage)
admin.site.register(models.TelegramAdmin)
admin.site.register(models.TelegramUser)
