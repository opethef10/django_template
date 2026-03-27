from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html


from .models import UserTopicSubscription, NotificationTopic
from ...utils import SelectRelatedModelAdmin


@admin.register(UserTopicSubscription)
class UserTopicSubscriptionAdmin(SelectRelatedModelAdmin):
    list_display = ('user', 'topic')
    search_fields = ('user__username', 'topic__key')


@admin.register(NotificationTopic)
class NotificationTopicAdmin(SelectRelatedModelAdmin):
    list_display = ('label', 'key',)
    readonly_fields = ('subscribed_users',)

    def subscribed_users(self, obj):
        """Return a list of subscribed users as clickable links."""
        users = obj.usertopicsubscription_set.prefetch_related('user').all()
        if not users:
            return "-"
        links = []
        for uts in users:
            user = uts.user
            url = reverse("admin:auth_user_change", args=[user.pk])
            links.append(f'<a href="{url}">{user.get_full_name()}</a>')
        return format_html(", ".join(links))

    subscribed_users.short_description = "Subscribed Users"
