from django.db import models
from django.contrib.auth.models import User

class ShortUrl(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name = "short_urls"
    )

    original_url = models.URLField()
    short_code = models.CharField(max_length=10)
    click_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(blank=True, null = True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"

