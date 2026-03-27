from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


class BaseUserProfileView(LoginRequiredMixin, TemplateView):
    pass


class UserProfileView(BaseUserProfileView):
    template_name = 'my_account.html'

    def get_user(self):
        return self.request.user


class UserAccountView(BaseUserProfileView):
    template_name = 'user_account.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.user = get_object_or_404(User, username=self.kwargs.get('username'))

    def get_user(self):
        return self.user
