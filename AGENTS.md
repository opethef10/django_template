# AGENTS.md

Guidelines for AI agents working with this Django template.

## Purpose

This is a **reusable Django template** designed for users to bootstrap new projects. When someone uses this template, they should be able to quickly set up a production-ready Django application with authentication, PWA support, internationalization, and PythonAnywhere deployment compatibility.

## Project Structure

This is **not** a traditional Django project. Key differences:

- **`src/` is the project root**, not the repository root
- Django settings, URLs, and WSGI/ASGI configs live in `src/settings/`
- Apps are in `src/apps/`, not in the repository root
- Static files exist both at project level (`src/static/`) and within apps (`src/apps/<app>/static/`)
- Templates exist both at project level (`src/templates/`) and within apps (`src/apps/<app>/templates/`)
- Apps should be created under `src/apps/`, not at root level

## Deployment Scripts

The `scripts/` folder contains deployment scripts optimized for **PythonAnywhere** compatibility:

| Script | Purpose |
|--------|---------|
| `scripts/test` | Run tests with test settings |
| `scripts/update.sh` | Full deployment update (backup, pull, install, migrate, collectstatic, reload) |
| `scripts/reload.sh` | Touch WSGI file to reload server |
| `scripts/backupdb.sh` | Database backup |
| `scripts/push` | Push to remote with submodule updates |
| `scripts/create_wsgi.sh` | Generate PythonAnywhere WSGI file |

## Git Workflow

This template uses **git flow** branching strategy:

- `main` - stable releases
- `develop` - integration branch
- `feature/*` - new features
- `hotfix/*` - urgent production fixes
- `release/*` - release preparation

## Changelog Strategy

Two changelog files work together:

| File | Purpose |
|------|---------|
| `CHANGELOG.md` | For the user's project (typically starts empty or minimal) |
| `TEMPLATE_CHANGELOG.md` | Documents template-level changes (versioned like `0.6.4`) |

When using this template, users should maintain their own `CHANGELOG.md` for project-specific changes while `TEMPLATE_CHANGELOG.md` tracks template evolution.

## Settings Architecture

Settings use a layered approach:

| File | Purpose |
|------|---------|
| `settings/_base.py` | Shared configuration (installed apps, middleware, templates, etc.) |
| `settings/development.py` | Local dev (DEBUG=True, DummyCache, console email, debug toolbar) |
| `settings/production.py` | Production (env vars for secrets, file logging, real email) |
| `settings/tests.py` | Test settings (fast, no migrations, disabled logging) |

**CRITICAL**: Never hardcode secrets in base settings. Use `python-decouple`:
```python
from decouple import config
SECRET_KEY = config('DJANGO_SECRET_KEY')
```

### Development vs Production Settings

**Development** (`manage.py` defaults to `src.settings.development`):
- `DEBUG = True`
- `ALLOWED_HOSTS = ["*"]`
- Dummy cache backend
- Console email backend (prints to terminal)
- Debug toolbar enabled

**Production**:
- `DEBUG = False`
- `SECRET_KEY` from environment
- `ALLOWED_HOSTS` from environment (comma-separated)
- File-based logging to `/var/www/proj.log`
- Real SMTP email (only if `EMAIL_ENABLED=True`)
- Static/media files served from `/var/www/`

### Test Settings (`src.settings.tests`)

Used for fast test execution:
- `PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]` (fast hashing)
- Migrations disabled via `DisableMigrations` class
- Logging disabled
- Recaptcha silenced

## Configuration

All configuration via `.env` file. See `.env.example` for required variables.

**Required for all environments:**
- `PROJECT_SLUG`, `PROJECT_NAME`, `PROJECT_DESCRIPTION`, `PROJECT_DOMAIN`
- `PROJECT_ADMIN_NAME`, `PROJECT_ADMIN_EMAIL`
- `DJANGO_SECRET_KEY`

**Required for production:**
- `DJANGO_ALLOWED_HOSTS` (comma-separated domain list)
- `DJANGO_EMAIL_*` if `DJANGO_EMAIL_ENABLED=True`

## Dependencies

Three requirement files, use `-r` to include:

| File | Use Case | Includes |
|------|----------|----------|
| `requirements/base.txt` | All environments | Core Django, allauth, PWA, recaptcha, etc. |
| `requirements/development.txt` | Local development | base.txt + django-debug-toolbar |
| `requirements/production.txt` | Production deployment | base.txt only |

**Install for development:**
```bash
pip install -r requirements/development.txt
```

## Key Production-Ready Features

### Security
- HTTPS enforcement via `SECURE_PROXY_SSL_HEADER`
- X-Frame-Options set to `SAMEORIGIN`
- CSRF protection enabled
- Secrets managed via environment variables, never committed

### Logging
- Verbose format with timestamps and timezone
- Console handler for development
- File handler (`/var/www/proj.log`) for production
- Logger named `proj` under `LOGGING['loggers']`

### Email
- Disabled by default, enable via `DJANGO_EMAIL_ENABLED=True`
- Gmail SMTP configuration in production
- Console backend in development (safe, no accidental sends)

### Static/Media Files
- Development: served from `src/static/` and `src/media/`
- Production: collected to `/var/www/static` and `/var/www/media`
- Apps can have their own `static/` folders (Django finds them automatically)

## Allauth Integration

This template uses `django-allauth` for authentication:
- Login via username or email (`ACCOUNT_LOGIN_METHODS`)
- Custom signup form with honeypot field (`src.forms.CustomSignupForm`)
- Custom account adapter: `src.adapters.CustomAccountAdapter`
- Session duration: 1 year by default

**Do not change AUTHENTICATION_BACKENDS** unless you also update the adapter.

## Custom Template Tags

Two custom template tag libraries:

| Library | Location | Purpose |
|---------|----------|---------|
| `form_tags` | `src/tags/form_tags.py` | Form rendering utilities |
| `menu_tags` | `src/tags/menu_tags.py` | Menu/navigation utilities |

Register in `TEMPLATES['OPTIONS']['libraries']` in `_base.py`.

## Context Processors

Two context processors automatically available in all templates:

| Name | Location | Purpose |
|------|----------|---------|
| `project_settings` | `src/context_processors/settings_values.py` | Exposes project config to templates |
| `menus` | `src/context_processors/menus.py` | Navigation menu data |

## PWA Support

Django PWA configured with:
- App name, description, theme colors from settings
- Icons expected at `/static/logo.png`
- Service worker at `src/static/js/serviceworker.js`
- Configured in `_base.py` under `PWA_APP_*` settings

## Internationalization

- Languages: English and Turkish
- Locale files in `src/locale/`
- Translation strings use `gettext_lazy`

## Apps Structure

Each app follows this pattern:
```
src/apps/<app_name>/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── views.py
├── urls.py
├── forms.py (optional)
├── signals.py (optional)
├── utils.py (optional)
├── tests/
│   ├── __init__.py
│   └── test_*.py
├── static/<app_name>/ (optional)
└── migrations/
    ├── __init__.py
    └── 0*.py
```

## Management Commands

Place custom commands in `<app>/management/commands/`.

## Testing

**Use test settings for faster execution:**
```bash
python manage.py test --settings=src.settings.tests
```

Or use the script:
```bash
./scripts/test
./scripts/test src.apps.subscriptions  # run specific app tests
```

## Common Patterns

### Adding a new app
1. Create under `src/apps/<app_name>/`
2. Add to `INSTALLED_APPS` in `settings/_base.py`
3. Include URLs in `src/urls.py` with `include('src.apps.<app_name>.urls')`

### Adding environment-specific settings
1. Define in `_base.py` with a default
2. Override in `development.py` or `production.py` as needed
3. Use `config()` for values that differ between environments

### Accessing settings in code
```python
from django.conf import settings

if settings.DEBUG:
    # development only code
```

### Project variables available everywhere
```python
from django.conf import settings

settings.PROJECT_NAME
settings.PROJECT_DOMAIN
settings.PROJECT_URL
settings.EMAIL_ENABLED
```
