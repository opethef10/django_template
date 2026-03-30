from django.urls import path

from .views import (
    DocumentationDeploymentView,
    DocumentationFeaturesView,
    DocumentationIndexView,
    DocumentationPythonanywhereView,
    DocumentationSettingsView,
    DocumentationSetupView,
    DocumentationStructureView,
    SearchView,
)

app_name = "example"

urlpatterns = [
    path("", DocumentationIndexView.as_view(), name="index"),
    path("", DocumentationIndexView.as_view(), name="home"),
    path("setup/", DocumentationSetupView.as_view(), name="setup"),
    path("structure/", DocumentationStructureView.as_view(), name="structure"),
    path("settings/", DocumentationSettingsView.as_view(), name="settings"),
    path("features/", DocumentationFeaturesView.as_view(), name="features"),
    path("deployment/", DocumentationDeploymentView.as_view(), name="deployment"),
    path("deployment/pythonanywhere/", DocumentationPythonanywhereView.as_view(), name="pythonanywhere"),
    path("api/search/", SearchView.as_view(), name="search"),
]
