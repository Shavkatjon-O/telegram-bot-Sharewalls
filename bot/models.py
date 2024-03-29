from django.db import models
from common.models import BaseModel


class LanguageChoices(models.TextChoices):
    RUSSIAN = "ru", "Russian"
    UZBEK = "uz", "Uzbek"


class Wallpaper(BaseModel):
    downloads_count = models.IntegerField(default=0)
    downloads_count_unique = models.IntegerField(default=0)

    auditory_language = models.CharField(max_length=2, choices=LanguageChoices.choices)

    def __str__(self):
        return self.auditory_language


class WallpaperImage(BaseModel):
    wallpaper = models.ForeignKey(Wallpaper, on_delete=models.CASCADE)

    file_id = models.CharField(max_length=256)

    def __str__(self):
        return self.file_id


class TelegramAdmin(BaseModel):
    user_id = models.BigIntegerField(unique=True)

    def __str__(self):
        return str(self.user_id)


class TelegramUser(BaseModel):
    user_id = models.BigIntegerField(unique=True)

    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    language = models.CharField(max_length=2, choices=LanguageChoices.choices)

    def __str__(self):
        return str(self.user_id)
