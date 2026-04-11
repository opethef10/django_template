from django.views.generic import TemplateView


class DocumentationIndexView(TemplateView):
    template_name = "docs/index.html"


class DocumentationSetupView(TemplateView):
    template_name = "docs/setup.html"


class DocumentationStructureView(TemplateView):
    template_name = "docs/structure.html"


class DocumentationSettingsView(TemplateView):
    template_name = "docs/settings.html"


class DocumentationCaptchaView(TemplateView):
    template_name = "docs/captcha.html"


class DocumentationEmailView(TemplateView):
    template_name = "docs/email.html"


class DocumentationFeaturesView(TemplateView):
    template_name = "docs/features.html"


class DocumentationDeploymentView(TemplateView):
    template_name = "docs/deployment.html"
