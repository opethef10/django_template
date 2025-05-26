from django import forms
from django.conf import settings
from django.utils.translation import gettext as _
from django_recaptcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="Ad")
    last_name = forms.CharField(max_length=50, label="Soyad")
    email = forms.EmailField(label="E-posta")
    message = forms.CharField(widget=forms.Textarea, label="Mesaj")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(settings.RECAPTCHA_ENABLED)
        if getattr(settings, 'RECAPTCHA_ENABLED', False):
            # Only add the ReCaptchaField if RECAPTCHA_ENABLED is True
            self.fields['captcha'] = ReCaptchaField(label=_("Captcha"))
