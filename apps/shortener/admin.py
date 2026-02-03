from django.contrib import admin
from .models import ShortUrl

@admin.register(ShortUrl)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = (
        "short_code",
        "original_url",
        "user",
        "click_count",
        "created_at",
        "expires_at",
        "is_active",
    )
    search_fields = ("short_code", "original_url", "user__username")
    list_filter = ("created_at", "is_active")
