from pathlib import Path

from decouple import config, Csv

from ._base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', cast=Csv())
CSRF_TRUSTED_ORIGINS = [f"https://{h}" for h in ALLOWED_HOSTS]
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

_VAR_DIR = Path("/var/www/")

STATIC_ROOT = _VAR_DIR / "static"
MEDIA_ROOT = _VAR_DIR / "media"
_LOG_PATH = _VAR_DIR / "proj.log"

EMAIL_ENABLED = config("DJANGO_EMAIL_ENABLED", cast=bool, default=False)
if EMAIL_ENABLED:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    SERVER_EMAIL = config("DJANGO_SERVER_EMAIL")
    EMAIL_HOST_USER = config("DJANGO_EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = config("DJANGO_EMAIL_HOST_PASSWORD")
    PROJECT_ADMIN_EMAILS = config("PROJECT_ADMIN_EMAILS", cast=Csv())
    ADMINS = [("", email) for email in PROJECT_ADMIN_EMAILS]

RECAPTCHA_ENABLED = config("RECAPTCHA_ENABLED", cast=bool, default=False)
if RECAPTCHA_ENABLED:
    RECAPTCHA_PUBLIC_KEY = config("RECAPTCHA_PUBLIC_KEY")
    RECAPTCHA_PRIVATE_KEY = config("RECAPTCHA_PRIVATE_KEY")
else:
    SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']

LOGGING['handlers']['file'] = {
    'level': 'INFO',
    'class': 'logging.FileHandler',
    'filename': _LOG_PATH,
    'formatter': 'verbose',
}
LOGGING['loggers']['proj']["handlers"] = ["file"]
