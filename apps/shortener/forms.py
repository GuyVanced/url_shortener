from django import forms
from .models import ShortUrl

class ShortUrlForm(forms.ModelForm):
    class Meta:
        model = ShortUrl
        fields = ["original_url"]