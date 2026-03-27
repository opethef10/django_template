from django import forms
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from mdeditor.fields import MDTextFormField

from .models import NotificationTopic, UserTopicSubscription


class UserSubscriptionForm(forms.Form):
    subscriptions = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label=_("E-Mail Subscriptions"),
    )

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        topics = NotificationTopic.objects.exclude(key="test")
        self.fields['subscriptions'].choices = [
            (
                t.key,
                format_html(
                    "{}<br><small class='text-muted'>{}</small>",
                    t.label,
                    t.explanation
                ) if t.explanation else t.label
            )
            for t in topics
        ]

        if user:
            existing = UserTopicSubscription.objects.filter(user=user)
            subscribed_keys = [s.topic.key for s in existing]
            self.initial['subscriptions'] = subscribed_keys

    def save(self, user):
        chosen_keys = self.cleaned_data.get('subscriptions', [])

        existing = UserTopicSubscription.objects.filter(user=user)
        existing_keys = [s.topic.key for s in existing]

        for s in existing:
            if s.topic.key not in chosen_keys:
                s.delete()

        all_topics = NotificationTopic.objects.all()
        for topic in all_topics:
            if topic.key in chosen_keys and topic.key not in existing_keys:
                UserTopicSubscription.objects.create(user=user, topic=topic)


class SendTopicMailForm(forms.Form):
    topic = forms.ModelChoiceField(
        queryset=NotificationTopic.objects.all(),
        required=True,
        label=_("Topic"),
    )
    subject = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label=_("Subject"),
    )
    message = MDTextFormField(
        label=_("Message"),
    )
