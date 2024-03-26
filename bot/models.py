from django.db import models
from common.models import BaseModel


class LanguageChoices(models.TextChoices):
    RUSSIAN = "ru", "Russian"
    UZBEK = "uz", "Uzbek"


class Wallpaper(BaseModel):
    downloads_count = models.IntegerField(default=0)
    downloads_count_unique = models.IntegerField(default=0)

    auditory_language = models.CharField(max_length=2, choices=LanguageChoices.choices)


class WallpaperImage(BaseModel):
    wallpaper = models.ForeignKey(Wallpaper, on_delete=models.CASCADE)

    file_id = models.CharField(max_length=256)


class TelegramAdmin(BaseModel):
    user_id = models.BigIntegerField(unique=True)


class TelegramUser(BaseModel):
    user_id = models.BigIntegerField(unique=True)

    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)


################# OLD MODELS #################


class FileMessage(models.Model):
    file_id = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=9, unique=True, null=True, blank=True)
    forward_message_id = models.IntegerField(null=True, blank=True)

    downloads = models.IntegerField(default=0)
    unique_downloads = models.IntegerField(default=0)

    downloads_second = models.IntegerField(default=0)
    unique_downloads_second = models.IntegerField(default=0)

    is_media_group = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Temp FileMessage"
        verbose_name_plural = "Temp FileMessages"


class MediaGroupItem(models.Model):
    file_message = models.ForeignKey(FileMessage, on_delete=models.CASCADE)

    file_id = models.CharField(max_length=255)
    file_content_type = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Temp MediaGroupItem"
        verbose_name_plural = "Temp MediaGroupItems"


class Admin(models.Model):
    user_id = models.BigIntegerField(unique=True)

    class Meta:
        verbose_name = "Temp Admin"
        verbose_name_plural = "Temp Admins"


class TGusers(models.Model):
    user_id = models.TextField()
    language = models.TextField()
    status = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Temp TGusers"
        verbose_name_plural = "Temp TGusers"
