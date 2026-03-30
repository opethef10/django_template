from django.views.generic import TemplateView


class DocumentationIndexView(TemplateView):
    template_name = "example/index.html"


class DocumentationSetupView(TemplateView):
    template_name = "example/setup.html"


class DocumentationStructureView(TemplateView):
    template_name = "example/structure.html"


class DocumentationSettingsView(TemplateView):
    template_name = "example/settings.html"


class DocumentationFeaturesView(TemplateView):
    template_name = "example/features.html"


class DocumentationDeploymentView(TemplateView):
    template_name = "example/deployment.html"


class DocumentationPythonanywhereView(TemplateView):
    template_name = "example/pythonanywhere.html"
