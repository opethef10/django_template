import mimetypes

from ._base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]
# CSRF_TRUSTED_ORIGINS = config('DJANGO_CSRF_TRUSTED_ORIGINS', cast=Csv())
# CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SILENCED_SYSTEM_CHECKS = [
    'django_recaptcha.recaptcha_test_key_error',
]

INSTALLED_APPS.extend(
    [
        "debug_toolbar",
        "django_removals",
    ]
)

MIDDLEWARE.insert(7, "debug_toolbar.middleware.DebugToolbarMiddleware")

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: DEBUG,
}

mimetypes.add_type("application/javascript", ".js", True)
