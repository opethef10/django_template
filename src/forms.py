from allauth.account.forms import SignupForm
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_recaptcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, label=_("Name"))
    last_name = forms.CharField(max_length=50, label=_("Surname"))
    email = forms.EmailField(label=_("Email Address"))
    message = forms.CharField(widget=forms.Textarea, label=_("Message"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if getattr(settings, 'RECAPTCHA_ENABLED', False):
            # Only add the ReCaptchaField if RECAPTCHA_ENABLED is True
            self.fields['captcha'] = ReCaptchaField(label=_("Captcha"))


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label=_("Name"))
    last_name = forms.CharField(max_length=30, label=_("Surname"))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
