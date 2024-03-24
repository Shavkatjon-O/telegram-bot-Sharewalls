from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "is_staff", "is_active", "created_at")
    list_display_links = ("username",)
