from django.apps import apps
from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMessage
from django.http import Http404, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView, View

from .forms import ContactForm


class HomeView(RedirectView):
    url = reverse_lazy('docs:index')


@method_decorator(cache_page(30 * settings.DAYS), name='dispatch')
class SearchView(View):
    def get(self, request, *args, **kwargs):
        results = []
        for app_config in apps.get_app_configs():
            if app_config.name.startswith('src.apps.'):
                try:
                    module = __import__(f'{app_config.name}.search', fromlist=['get_search_results'])
                    if hasattr(module, 'get_search_results'):
                        results.extend(module.get_search_results())
                except Exception:
                    pass
        return JsonResponse({'results': results})


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_message = _("Your message has been sent successfully!")
    error_message = _(
        "The form could not be sent, please correct the form errors and try again!"
    )
    success_url = reverse_lazy('contact')
    subject = _("Contact Us")

    def dispatch(self, request, *args, **kwargs):
        if not getattr(settings, 'DEBUG', False):
            if not getattr(settings, 'EMAIL_ENABLED', False):
                raise Http404(_("Contact page is disabled."))
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user  # Get the currently logged-in user

        # Check if the user is authenticated and populate the initial data
        if user.is_authenticated:
            initial['first_name'] = user.first_name
            initial['last_name'] = user.last_name
            initial['email'] = user.email

        return initial

    def form_valid(self, form):
        first_name, last_name, mail_address = [
            form.cleaned_data['first_name'].strip(),
            form.cleaned_data['last_name'].strip(),
            form.cleaned_data['email'].strip(),
        ]

        # Use EmailMessage instead of send_mail
        admin_emails = [email for _, email in settings.ADMINS]

        prefix = settings.EMAIL_SUBJECT_PREFIX
        email = EmailMessage(
            subject=f"{prefix}{self.subject} - {first_name} {last_name}",
            body=form.cleaned_data['message'].strip(),
            from_email=None,  # You can specify a from address here if needed
            to=admin_emails,  # Use the admin emails from settings.
            reply_to=[mail_address]
        )

        # Send the email
        email.send(fail_silently=False)
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, self.error_message)
        return response
