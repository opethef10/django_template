from django.urls import reverse_lazy


def get_search_results():
    return [
        {
            "url": reverse_lazy("example:index"),
            "search_text": "Documentation Home",
            "search_tokens": ["documentation", "docs", "home", "index", "guide", "welcome"],
            "category": "Documentation",
            "sub_links": [
                {"url": reverse_lazy("example:setup"), "label": "Setup"},
                {"url": reverse_lazy("example:structure"), "label": "Structure"},
                {"url": reverse_lazy("example:settings"), "label": "Settings"},
                {"url": reverse_lazy("example:features"), "label": "Features"},
                {"url": reverse_lazy("example:deployment"), "label": "Deployment"},
            ]
        },
        {
            "url": reverse_lazy("example:setup"),
            "search_text": "Setup Guide",
            "search_tokens": ["setup", "install", "docker", "manual", "venv", "virtual environment", "clone", "git", "environment", "install dependencies"],
            "category": "Documentation",
            "sub_links": [
                {"url": reverse_lazy("example:setup") + "#docker", "label": "Docker"},
                {"url": reverse_lazy("example:setup") + "#manual", "label": "Manual"},
            ]
        },
        {
            "url": reverse_lazy("example:structure"),
            "search_text": "Project Structure",
            "search_tokens": ["structure", "directory", "project", "files", "folders", "apps", "templates", "static", "settings"],
            "category": "Documentation",
            "sub_links": [
                {"url": reverse_lazy("example:structure") + "#overview", "label": "Overview"},
                {"url": reverse_lazy("example:structure") + "#apps-structure", "label": "App Structure"},
                {"url": reverse_lazy("example:structure") + "#adding-app", "label": "Adding App"},
            ]
        },
        {
            "url": reverse_lazy("example:settings"),
            "search_text": "Settings & Configuration",
            "search_tokens": ["settings", "configuration", "environment", "variables", ".env", "development", "production"],
            "category": "Documentation",
            "sub_links": [
                {"url": reverse_lazy("example:settings") + "#architecture", "label": "Architecture"},
                {"url": reverse_lazy("example:settings") + "#installed-apps", "label": "Installed Apps"},
                {"url": reverse_lazy("example:settings") + "#captcha", "label": "Captcha"},
                {"url": reverse_lazy("example:settings") + "#menu-config", "label": "Menus"},
            ]
        },
        {
            "url": reverse_lazy("example:captcha"),
            "search_text": "Captcha Setup Guide",
            "search_tokens": ["captcha", "recaptcha", "spam", "protection", "google", "api key", "bot"],
            "category": "Documentation",
            "sub_links": [
                {"url": reverse_lazy("example:captcha") + "#overview", "label": "Overview"},
                {"url": reverse_lazy("example:captcha") + "#getting-keys", "label": "Getting Keys"},
                {"url": reverse_lazy("example:captcha") + "#setup", "label": "Setup"},
                {"url": reverse_lazy("example:captcha") + "#how-it-works", "label": "How It Works"},
            ]
        },
        {
            "url": reverse_lazy("example:email"),
            "search_text": "Email Setup Guide",
            "search_tokens": ["email", "gmail", "smtp", "app password", "notifications", "password reset"],
            "category": "Documentation",
            "sub_links": [
                {"url": reverse_lazy("example:email") + "#overview", "label": "Overview"},
                {"url": reverse_lazy("example:email") + "#gmail-setup", "label": "Gmail Setup"},
                {"url": reverse_lazy("example:email") + "#project-settings", "label": "Project Settings"},
                {"url": reverse_lazy("example:email") + "#testing", "label": "Testing"},
            ]
        },
        {
            "url": reverse_lazy("example:features"),
            "search_text": "Built-in Features",
            "search_tokens": ["features", "bootstrap", "datatables", "datatable", "icons", "font awesome", "dark mode", "pwa", "authentication", "flatpages", "markdown", "recaptcha", "i18n", "internationalization"],
            "category": "Documentation",
            "sub_links": [
                {"url": reverse_lazy("example:features") + "#frontend", "label": "Frontend"},
                {"url": reverse_lazy("example:features") + "#backend", "label": "Backend"},
                {"url": reverse_lazy("example:features") + "#pwa", "label": "PWA"},
                {"url": reverse_lazy("example:features") + "#i18n", "label": "i18n"},
            ]
        },
        {
            "url": reverse_lazy("example:deployment"),
            "search_text": "Deployment",
            "search_tokens": ["deployment", "deploy", "production", "server", "hosting", "pythonanywhere"],
            "category": "Documentation",
            "sub_links": [
                {"url": reverse_lazy("example:deployment") + "#requirements", "label": "Requirements"},
                {"url": reverse_lazy("example:deployment") + "#deployment-checklist", "label": "Checklist"},
                {"url": reverse_lazy("example:deployment") + "#scripts", "label": "Scripts"},
            ]
        },
        {
            "url": reverse_lazy("example:pythonanywhere"),
            "search_text": "PythonAnywhere Deployment Guide",
            "search_tokens": ["pythonanywhere", "python anywhere", "deploy", "deployment", "wsgi", "web app", "static files", "database", "migrate", "domain", "custom domain"],
            "category": "Documentation",
            "sub_links": [
                {"url": reverse_lazy("example:pythonanywhere") + "#prerequisites", "label": "Prerequisites"},
                {"url": reverse_lazy("example:pythonanywhere") + "#step1", "label": "Console Setup"},
                {"url": reverse_lazy("example:pythonanywhere") + "#step2", "label": "Environment"},
                {"url": reverse_lazy("example:pythonanywhere") + "#step3", "label": "Migrations"},
                {"url": reverse_lazy("example:pythonanywhere") + "#step4", "label": "Static Files"},
                {"url": reverse_lazy("example:pythonanywhere") + "#step5", "label": "Web App Config"},
                {"url": reverse_lazy("example:pythonanywhere") + "#troubleshooting", "label": "Troubleshooting"},
            ]
        },
    ]
