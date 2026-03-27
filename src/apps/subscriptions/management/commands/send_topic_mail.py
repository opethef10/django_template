from django.core.management.base import BaseCommand, CommandError
from django.core.mail import EmailMessage
from django.conf import settings

from ...models import NotificationTopic
from ...utils import build_subscription_footer


class Command(BaseCommand):
    help = "Send an email to all users subscribed to a specific notification topic."

    def add_arguments(self, parser):
        parser.add_argument(
            "topic_key",
            type=str,
            help="Key of the topic to send mail for."
        )
        parser.add_argument(
            "--subject",
            type=str,
            default="Test subject",
            help="Subject of the email."
        )
        parser.add_argument(
            "--message",
            type=str,
            default="This is a test notification.",
            help="Body of the email."
        )

    def handle(self, *args, **options):
        topic_key = options["topic_key"]
        subject = options['subject']
        message = options['message']

        try:
            topic = NotificationTopic.objects.get(key=topic_key)
        except NotificationTopic.DoesNotExist:
            raise CommandError(f"Topic '{topic_key}' does not exist.")

        subscribers = [
            uts.user.email
            for uts
            in topic.usertopicsubscription_set.prefetch_related('user').all()
        ]

        if not subscribers:
            self.stdout.write(self.style.WARNING("No subscribers for this topic."))
            return

        footer = build_subscription_footer(topic.label)
        message += f"\n{footer}"

        # Send email using BCC to preserve privacy
        email = EmailMessage(
            subject=f"{settings.EMAIL_SUBJECT_PREFIX}{subject}",
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.DEFAULT_FROM_EMAIL],
            bcc=subscribers,
        )
        email.send(fail_silently=False)

        self.stdout.write(
            self.style.SUCCESS(
                f"Email sent to {len(subscribers)} subscribers of '{topic_key}'."
            )
        )
