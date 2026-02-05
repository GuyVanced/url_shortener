from django.db import models
from django.contrib.auth.models import User
import os

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
    
    # QR Code related fields
    qr_code_image = models.ImageField(
        upload_to='qr_codes/',
        blank=True,
        null=True,
        help_text="Generated QR code image"
    )
    qr_code_generated_at = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Timestamp when QR code was generated"
    )

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"

    @property
    def has_qr_code(self):
        """Check if QR code has been generated for this URL"""
        return bool(self.qr_code_image and self.qr_code_generated_at)
    
    def delete(self, *args, **kwargs):
        """Override delete to clean up QR code file"""
        if self.qr_code_image:
            try:
                if os.path.isfile(self.qr_code_image.path):
                    os.remove(self.qr_code_image.path)
            except Exception as e:
                print(f"Error deleting QR code file: {e}")
        super().delete(*args, **kwargs)

