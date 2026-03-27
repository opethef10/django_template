from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import FormView
from markdown import markdown

from .forms import SendTopicMailForm, UserSubscriptionForm
from .models import UserTopicSubscription
from .utils import build_subscription_footer


class SubscriptionUpdateView(SuccessMessageMixin, LoginRequiredMixin, FormView):
    form_class = UserSubscriptionForm
    template_name = 'subscriptions/update.html'
    success_url = reverse_lazy('subscriptions:update')
    success_message = _("Your subscriptions have been successfully updated!")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save(self.request.user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subscriptions'] = UserTopicSubscription.objects.filter(
            user=self.request.user
        ).select_related('topic')
        return context


class SendTopicMailView(UserPassesTestMixin, SuccessMessageMixin, FormView):
    template_name = "subscriptions/send_topic_mail.html"
    form_class = SendTopicMailForm
    success_url = reverse_lazy("subscriptions:send")
    success_message = _("Email sent successfully.")
    error_message = _("An error occurred while submitting the form. Please try again.")

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        topic = form.cleaned_data["topic"]
        subject = form.cleaned_data["subject"].strip()
        message = form.cleaned_data["message"].strip()

        # Get emails of all subscribers
        subscriber_emails = list(
            UserTopicSubscription.objects.filter(topic=topic)
            .select_related("user")
            .values_list("user__email", flat=True)
        )

        if not subscriber_emails:
            messages.warning(self.request, "No users subscribed to this topic.")
            return super().form_invalid(form)

        footer = build_subscription_footer(topic.label)
        message += f"\n\n{footer}"

        # Convert markdown to HTML
        message_html = markdown(
            message,
            extensions=["extra", "sane_lists", "nl2br"]
        )

        email = EmailMultiAlternatives(
            subject=f"{settings.EMAIL_SUBJECT_PREFIX}{subject}",
            body=message,  # plain text fallback
            from_email=None,        # Use default from settings
            to=[settings.SERVER_EMAIL],  # Send to server email
            bcc=subscriber_emails,   # All subscribers
        )

        email.attach_alternative(message_html, "text/html")
        email.send(fail_silently=False)
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, self.error_message)
        return response
