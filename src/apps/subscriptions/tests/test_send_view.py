from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core import mail
from django.contrib.messages import get_messages
from django.conf import settings

from ..models import NotificationTopic, UserTopicSubscription

User = get_user_model()


class SendTopicMailViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("subscriptions:send")

        # Topics
        self.topic_general = NotificationTopic.objects.create(
            key="general", label="General"
        )
        self.topic_news = NotificationTopic.objects.create(
            key="news", label="News"
        )

        # Users
        self.superuser = User.objects.create_superuser(
            username="admin", email="admin@example.com", password="pw"
        )
        self.user1 = User.objects.create_user(
            username="u1", email="u1@example.com", password="pw"
        )
        self.user2 = User.objects.create_user(
            username="u2", email="u2@example.com", password="pw"
        )

    def test_signal_creates_subscriptions_on_user_creation(self):
        """Test that subscriptions are automatically created for new users."""
        # Clear subscriptions for user2 to test signal worked
        UserTopicSubscription.objects.filter(user=self.user2).delete()

        # Verify user2 has no subscriptions
        self.assertEqual(
            UserTopicSubscription.objects.filter(user=self.user2).count(),
            0
        )

        # Create a new user - signal should auto-subscribe
        new_user = User.objects.create_user(
            username="newuser", email="new@example.com", password="pw"
        )

        # Check that subscriptions were created for the new user
        subs = UserTopicSubscription.objects.filter(user=new_user)
        self.assertTrue(subs.exists())
        # Should have subscriptions for all topics
        topic_keys = set(s.topic.key for s in subs)
        self.assertIn("general", topic_keys)
        self.assertIn("news", topic_keys)

    def test_requires_superuser(self):
        self.client.login(username="u1", password="pw")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_superuser_can_load_view(self):
        self.client.login(username="admin", password="pw")
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Topic")     # field label
        self.assertContains(response, "Message")
        self.assertContains(response, "Type")

    def test_valid_form_sends_mail_via_server_email_and_bcc(self):
        self.client.login(username="admin", password="pw")

        data = {
            "topic": self.topic_general.pk,
            "subject": "Test Subject",
            "message": "Hello world",
        }

        response = self.client.post(self.url, data, follow=True)

        # success
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)

        sent = mail.outbox[0]

        # TO must be SERVER_EMAIL
        self.assertEqual(sent.to, [settings.SERVER_EMAIL])

        # All users are subscribed to general topic via signal (admin, u1, u2)
        self.assertEqual(
            set(sent.bcc),
            {"admin@example.com", "u1@example.com", "u2@example.com"}
        )

        # footer must be appended
        self.assertIn("Hello world", sent.body)
        self.assertIn("subscribed", sent.body.lower())

        # success message exists
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("successfully" in m.message.lower() for m in messages))

    def test_invalid_form_renders_template_and_shows_errors(self):
        self.client.login(username="admin", password="pw")

        response = self.client.post(self.url, {}, follow=True)

        self.assertEqual(response.status_code, 200)

        # error message from form
        self.assertContains(response, "This field is required.")

        # no mail sent
        self.assertEqual(len(mail.outbox), 0)

    def test_no_subscribers_shows_warning_and_does_not_send(self):
        self.client.login(username="admin", password="pw")

        # remove all subscribers for general
        UserTopicSubscription.objects.filter(topic=self.topic_general).delete()

        data = {
            "topic": self.topic_general.pk,
            "subject": "Empty Test",
            "message": "Nothing here",
        }

        response = self.client.post(self.url, data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 0)

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(
            any("no users subscribed" in m.message.lower() for m in messages)
        )
