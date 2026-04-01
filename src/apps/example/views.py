from django.http import JsonResponse
from django.views.generic import TemplateView


SEARCH_RESULTS = {
    "results": [
        {
            "url": "/",
            "search_text": "Documentation Home",
            "search_tokens": ["documentation", "docs", "home", "index", "guide", "welcome"],
            "category": "Documentation",
            "sub_links": [
                {"url": "/setup/", "label": "Setup"},
                {"url": "/structure/", "label": "Structure"},
                {"url": "/settings/", "label": "Settings"},
                {"url": "/features/", "label": "Features"},
                {"url": "/deployment/", "label": "Deployment"},
            ]
        },
        {
            "url": "/setup/",
            "search_text": "Setup Guide",
            "search_tokens": ["setup", "install", "docker", "manual", "venv", "virtual environment", "clone", "git", "environment", "install dependencies"],
            "category": "Documentation",
            "sub_links": [
                {"url": "/setup/#docker", "label": "Docker"},
                {"url": "/setup/#manual", "label": "Manual"},
            ]
        },
        {
            "url": "/structure/",
            "search_text": "Project Structure",
            "search_tokens": ["structure", "directory", "project", "files", "folders", "apps", "templates", "static", "settings"],
            "category": "Documentation",
            "sub_links": [
                {"url": "/structure/#overview", "label": "Overview"},
                {"url": "/structure/#apps-structure", "label": "App Structure"},
                {"url": "/structure/#adding-app", "label": "Adding App"},
            ]
        },
        {
            "url": "/settings/",
            "search_text": "Settings & Configuration",
            "search_tokens": ["settings", "configuration", "environment", "variables", ".env", "development", "production"],
            "category": "Documentation",
            "sub_links": [
                {"url": "/settings/#architecture", "label": "Architecture"},
                {"url": "/settings/#installed-apps", "label": "Installed Apps"},
                {"url": "/settings/#captcha", "label": "Captcha"},
                {"url": "/settings/#menu-config", "label": "Menus"},
            ]
        },
        {
            "url": "/features/captcha/",
            "search_text": "Captcha Setup Guide",
            "search_tokens": ["captcha", "recaptcha", "spam", "protection", "google", "api key", "bot"],
            "category": "Documentation",
            "sub_links": [
                {"url": "/features/captcha/#overview", "label": "Overview"},
                {"url": "/features/captcha/#getting-keys", "label": "Getting Keys"},
                {"url": "/features/captcha/#setup", "label": "Setup"},
                {"url": "/features/captcha/#how-it-works", "label": "How It Works"},
            ]
        },
        {
            "url": "/features/email/",
            "search_text": "Email Setup Guide",
            "search_tokens": ["email", "gmail", "smtp", "app password", "notifications", "password reset"],
            "category": "Documentation",
            "sub_links": [
                {"url": "/features/email/#overview", "label": "Overview"},
                {"url": "/features/email/#gmail-setup", "label": "Gmail Setup"},
                {"url": "/features/email/#project-settings", "label": "Project Settings"},
                {"url": "/features/email/#testing", "label": "Testing"},
            ]
        },
        {
            "url": "/features/",
            "search_text": "Built-in Features",
            "search_tokens": ["features", "bootstrap", "datatables", "datatable", "icons", "font awesome", "dark mode", "pwa", "authentication", "flatpages", "markdown", "recaptcha", "i18n", "internationalization"],
            "category": "Documentation",
            "sub_links": [
                {"url": "/features/#frontend", "label": "Frontend"},
                {"url": "/features/#backend", "label": "Backend"},
                {"url": "/features/#pwa", "label": "PWA"},
                {"url": "/features/#i18n", "label": "i18n"},
            ]
        },
        {
            "url": "/deployment/",
            "search_text": "Deployment",
            "search_tokens": ["deployment", "deploy", "production", "server", "hosting", "pythonanywhere"],
            "category": "Documentation",
            "sub_links": [
                {"url": "/deployment/#requirements", "label": "Requirements"},
                {"url": "/deployment/#deployment-checklist", "label": "Checklist"},
                {"url": "/deployment/#scripts", "label": "Scripts"},
            ]
        },
        {
            "url": "/deployment/pythonanywhere/",
            "search_text": "PythonAnywhere Deployment Guide",
            "search_tokens": ["pythonanywhere", "python anywhere", "deploy", "deployment", "wsgi", "web app", "static files", "database", "migrate", "domain", "custom domain"],
            "category": "Documentation",
            "sub_links": [
                {"url": "/deployment/pythonanywhere/#prerequisites", "label": "Prerequisites"},
                {"url": "/deployment/pythonanywhere/#step1", "label": "Console Setup"},
                {"url": "/deployment/pythonanywhere/#step2", "label": "Environment"},
                {"url": "/deployment/pythonanywhere/#step3", "label": "Migrations"},
                {"url": "/deployment/pythonanywhere/#step4", "label": "Static Files"},
                {"url": "/deployment/pythonanywhere/#step5", "label": "Web App Config"},
                {"url": "/deployment/pythonanywhere/#troubleshooting", "label": "Troubleshooting"},
            ]
        },
    ]
}


class SearchView(TemplateView):
    template_name = "example/search.json"

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(SEARCH_RESULTS)


class DocumentationIndexView(TemplateView):
    template_name = "example/index.html"


class DocumentationSetupView(TemplateView):
    template_name = "example/setup.html"


class DocumentationStructureView(TemplateView):
    template_name = "example/structure.html"


class DocumentationSettingsView(TemplateView):
    template_name = "example/settings.html"


class DocumentationCaptchaView(TemplateView):
    template_name = "example/captcha.html"


class DocumentationEmailView(TemplateView):
    template_name = "example/email.html"


class DocumentationFeaturesView(TemplateView):
    template_name = "example/features.html"


class DocumentationDeploymentView(TemplateView):
    template_name = "example/deployment.html"


class DocumentationPythonanywhereView(TemplateView):
    template_name = "example/pythonanywhere.html"
