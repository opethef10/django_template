from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class NotificationTopic(models.Model):
    key = models.CharField(max_length=64, unique=True)
    label = models.CharField(max_length=128)
    explanation = models.TextField(blank=True, default="")

    def __str__(self):
        return self.label


class UserTopicSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscribed_topics")
    topic = models.ForeignKey(NotificationTopic, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "topic")

    def __str__(self):
        return f"{self.user} - {self.topic}"
