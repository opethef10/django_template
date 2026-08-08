from decouple import config, Csv

from ._base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', cast=Csv())

STATIC_ROOT = VAR_DIR / "static"
MEDIA_ROOT = VAR_DIR / "media"
_LOG_PATH = VAR_DIR / "proj.log"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

EMAIL_ENABLED = config("DJANGO_EMAIL_ENABLED", cast=bool, default=False)
if EMAIL_ENABLED:
    MAILERS = {
        "default": {
            "BACKEND": "django.core.mail.backends.smtp.EmailBackend",
            "OPTIONS": {
                "host": config("DJANGO_EMAIL_HOST", default="smtp.gmail.com"),
                "port": config("DJANGO_EMAIL_PORT", cast=int, default=587),
                "username": config("DJANGO_EMAIL_HOST_USER"),
                "password": config("DJANGO_EMAIL_HOST_PASSWORD"),
                "use_tls": config("DJANGO_EMAIL_USE_TLS", cast=bool, default=True),
            }
        }
    }
    SERVER_EMAIL = config("DJANGO_SERVER_EMAIL")
    ADMINS = config("PROJECT_ADMIN_EMAILS", cast=Csv())

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
