import mimetypes

from ._base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "INSECURE_DJANGO_SECRET_KEY_TO_BE_USED_AT_LOCAL_ENV"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]", f"{PROJECT_SLUG}.local"]
# CSRF_TRUSTED_ORIGINS = config('DJANGO_CSRF_TRUSTED_ORIGINS', cast=Csv())
# CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# For Docker
# `debug` is only True in templates if the vistor IP is in INTERNAL_IPS.
INTERNAL_IPS = type(
    str("c"), (), {"__contains__": lambda *a: True, "copy": lambda self: self}
)()

SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS.extend(
    [
        "debug_toolbar",
    ]
)

MIDDLEWARE.insert(5, "debug_toolbar.middleware.DebugToolbarMiddleware")

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

mimetypes.add_type("application/javascript", ".js", True)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    # 'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG
}
