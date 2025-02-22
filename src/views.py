from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMessage
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import ContactForm


class HomeView(TemplateView):
    template_name = "home.html"


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_message = _("Your message has been sent successfully!")
    error_message = _("The form could not be sent, please correct the form errors and try again!")
    success_url = reverse_lazy('contact')
    subject = _("Contact Us")

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
        admin_emails = [email for name, email in settings.ADMINS]  # Extract emails from ADMINS

        email = EmailMessage(
            subject=f"{settings.EMAIL_SUBJECT_PREFIX}{self.subject} - {first_name} {last_name}",
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
