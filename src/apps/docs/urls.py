from django.urls import path

from .views import (
    DocumentationCaptchaView,
    DocumentationDeploymentView,
    DocumentationEmailView,
    DocumentationFeaturesView,
    DocumentationIndexView,
    DocumentationSettingsView,
    DocumentationSetupView,
    DocumentationStructureView,
)

app_name = "docs"

urlpatterns = [
    path("", DocumentationIndexView.as_view(), name="index"),
    path("setup/", DocumentationSetupView.as_view(), name="setup"),
    path("structure/", DocumentationStructureView.as_view(), name="structure"),
    path("settings/", DocumentationSettingsView.as_view(), name="settings"),
    path("features/captcha/", DocumentationCaptchaView.as_view(), name="captcha"),
    path("features/email/", DocumentationEmailView.as_view(), name="email"),
    path("features/", DocumentationFeaturesView.as_view(), name="features"),
    path("deployment/", DocumentationDeploymentView.as_view(), name="deployment"),
]
