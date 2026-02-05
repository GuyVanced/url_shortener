from django import forms
from .models import ShortUrl
from django.utils import timezone

class ShortUrlForm(forms.ModelForm):
    use_custom_code = forms.BooleanField(
        required=False,
        label="Custom short code",
        help_text="Check to enter your own short code"
    )

    custom_short_code = forms.CharField(
        min_length=6,
        max_length=10,
        required=False,
        label= "Custom short code",
        help_text = "Enter a custom short code (max 10 characters)",
    )
    set_expiration = forms.BooleanField(
        required=False,
        label= "Set expiration time",
        help_text = "Check to set expiration date/time"
    )
    expires_at = forms.DateTimeField(
        required=False,
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"},
            format="%Y-%m-%dT%H:%M"
        ),
        label="Expiration date/time",
    )

    class Meta:
        model = ShortUrl
        fields = ["original_url", "expires_at"]
        
        labels = {
            "original_url": "Original URL",
        }

    def clean_custom_short_code(self):
        use_custom = self.cleaned_data.get("use_custom_code")
        code = self.cleaned_data.get("custom_short_code")
        if use_custom:
            if not code:
                raise forms.ValidationError("You must enter a custom code if checked.")
            if ShortUrl.objects.filter(short_code=code).exists():
                raise forms.ValidationError("This short code is already taken.")
        else:
            # Checkbox not checked → ignore the text input
            code = None
        return code

    def clean_expires_at(self):
        expires_at = self.cleaned_data.get("expires_at")
        set_exp = self.cleaned_data.get("set_expiration")
        if set_exp:
            if not expires_at:
                raise forms.ValidationError("You must select a date/time if expiration is enabled.")
            if expires_at <= timezone.now():
                raise forms.ValidationError("Expiration date/time must be in the future.")
        else:
            # Not setting expiration → ignore input
            expires_at = None
        return expires_at

class ShortUrlEditForm(forms.ModelForm):
    class Meta:
        model = ShortUrl
        fields = ["original_url", "expires_at", "is_active"]