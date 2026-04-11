from django.urls import reverse_lazy


def get_search_results():
    return [
        {
            "url": reverse_lazy("docs:index"),
            "search_text": "Documentation Home",
            "search_tokens": ["documentation", "docs", "home", "index", "guide", "welcome"],
            "category": "Documentation",
            "sub_links": [
                {"url": reverse_lazy("docs:setup"), "label": "Setup"},
                {"url": reverse_lazy("docs:structure"), "label": "Structure"},
                {"url": reverse_lazy("docs:settings"), "label": "Settings"},
                {"url": reverse_lazy("docs:features"), "label": "Features"},
                {"url": reverse_lazy("docs:deployment"), "label": "Deployment"},
            ]
        },
        {
            "url": reverse_lazy("docs:setup"),
            "search_text": "Setup Guide",
            "search_tokens": ["setup", "install", "docker", "manual", "venv", "virtual environment", "clone", "git", "environment", "install dependencies"],
            "category": "Documentation",
            "sub_links": [
                {"url": reverse_lazy("docs:setup") + "#docker", "label": "Docker"},
                {"url": reverse_lazy("docs:setup") + "#manual", "label": "Manual"},
            ]
        },
        {
            "url": reverse_lazy("docs:structure"),
            "search_text": "Project Structure",
            "search_tokens": ["structure", "directory", "project", "files", "folders", "apps", "templates", "static", "settings"],
            "category": "Documentation",
            "sub_links": [
                {"url": reverse_lazy("docs:structure") + "#overview", "label": "Overview"},
                {"url": reverse_lazy("docs:structure") + "#apps-structure", "label": "App Structure"},
                {"url": reverse_lazy("docs:structure") + "#adding-app", "label": "Adding App"},
            ]
        },
        {
            "url": reverse_lazy("docs:settings"),
            "search_text": "Settings & Configuration",
            "search_tokens": ["settings", "configuration", "environment", "variables", ".env", "development", "production"],
            "category": "Documentation",
            "sub_links": [
                {"url": reverse_lazy("docs:settings") + "#architecture", "label": "Architecture"},
                {"url": reverse_lazy("docs:settings") + "#installed-apps", "label": "Installed Apps"},
                {"url": reverse_lazy("docs:settings") + "#captcha", "label": "Captcha"},
                {"url": reverse_lazy("docs:settings") + "#menu-config", "label": "Menus"},
            ]
        },
        {
            "url": reverse_lazy("docs:captcha"),
            "search_text": "Captcha Setup Guide",
            "search_tokens": ["captcha", "recaptcha", "spam", "protection", "google", "api key", "bot"],
            "category": "Documentation",
            "sub_links": [
                {"url": reverse_lazy("docs:captcha") + "#overview", "label": "Overview"},
                {"url": reverse_lazy("docs:captcha") + "#getting-keys", "label": "Getting Keys"},
                {"url": reverse_lazy("docs:captcha") + "#setup", "label": "Setup"},
                {"url": reverse_lazy("docs:captcha") + "#how-it-works", "label": "How It Works"},
            ]
        },
        {
            "url": reverse_lazy("docs:email"),
            "search_text": "Email Setup Guide",
            "search_tokens": ["email", "gmail", "smtp", "app password", "notifications", "password reset"],
            "category": "Documentation",
            "sub_links": [
                {"url": reverse_lazy("docs:email") + "#overview", "label": "Overview"},
                {"url": reverse_lazy("docs:email") + "#gmail-setup", "label": "Gmail Setup"},
                {"url": reverse_lazy("docs:email") + "#project-settings", "label": "Project Settings"},
                {"url": reverse_lazy("docs:email") + "#testing", "label": "Testing"},
            ]
        },
        {
            "url": reverse_lazy("docs:features"),
            "search_text": "Built-in Features",
            "search_tokens": ["features", "bootstrap", "datatables", "datatable", "icons", "font awesome", "dark mode", "pwa", "authentication", "flatpages", "markdown", "recaptcha", "i18n", "internationalization"],
            "category": "Documentation",
            "sub_links": [
                {"url": reverse_lazy("docs:features") + "#frontend", "label": "Frontend"},
                {"url": reverse_lazy("docs:features") + "#backend", "label": "Backend"},
                {"url": reverse_lazy("docs:features") + "#pwa", "label": "PWA"},
                {"url": reverse_lazy("docs:features") + "#i18n", "label": "i18n"},
            ]
        },
        {
            "url": reverse_lazy("docs:deployment"),
            "search_text": "Deployment",
            "search_tokens": ["deployment", "deploy", "production", "server", "hosting", "pythonanywhere", "wsgi", "web app", "static files", "database", "migrate", "api token", "virtualenv"],
            "category": "Documentation",
            "sub_links": [
                {"url": reverse_lazy("docs:deployment") + "#prerequisites", "label": "Prerequisites"},
                {"url": reverse_lazy("docs:deployment") + "#setup", "label": "Setup"},
                {"url": reverse_lazy("docs:deployment") + "#deployment", "label": "Automatic Deployment"},
                {"url": reverse_lazy("docs:deployment") + "#troubleshooting", "label": "Troubleshooting"},
                {"url": reverse_lazy("docs:deployment") + "#requirements", "label": "Requirements"},
                {"url": reverse_lazy("docs:deployment") + "#scripts", "label": "Scripts"},
            ]
        },
    ]
