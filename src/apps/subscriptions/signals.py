from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import NotificationTopic, UserTopicSubscription

User = get_user_model()


@receiver(post_save, sender=User)
def create_default_subscriptions(sender, instance, created, **kwargs):
    if not created:
        return

    existing_subscriptions = UserTopicSubscription.objects.filter(
        user=instance,
    ).values_list('topic_id', flat=True)

    topics = NotificationTopic.objects.exclude(key="test")
    subscriptions_to_create = [
        UserTopicSubscription(user=instance, topic=topic)
        for topic in topics
        if topic.id not in existing_subscriptions
    ]

    UserTopicSubscription.objects.bulk_create(subscriptions_to_create, ignore_conflicts=True)
