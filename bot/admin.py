from django.contrib import admin
from . import models

admin.site.register(models.FileMessage)
admin.site.register(models.MediaGroupItem)
admin.site.register(models.Admin)
admin.site.register(models.TGusers)
