from django.urls import path

from .views import SendTopicMailView, SubscriptionUpdateView

app_name = "subscriptions"

urlpatterns = [
    path("send/", SendTopicMailView.as_view(), name="send"),
    path('update/', SubscriptionUpdateView.as_view(), name='update'),
]
