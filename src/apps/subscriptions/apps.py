from django.apps import AppConfig


class SubscriptionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.apps.subscriptions'

    def ready(self):
        import src.apps.subscriptions.signals  # noqa
