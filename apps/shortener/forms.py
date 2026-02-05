from django import forms
from .models import ShortUrl

class ShortUrlForm(forms.ModelForm):
    class Meta:
        model = ShortUrl
        fields = ["original_url"]

class ShortUrlEditForm(forms.ModelForm):
    class Meta:
        model = ShortUrl
        fields = ["original_url", "expires_at", "is_active"]