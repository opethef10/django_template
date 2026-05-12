from pathlib import Path

from .production import *


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
] + [m for m in MIDDLEWARE if m != 'django.middleware.security.SecurityMiddleware']

_VAR_DIR = Path("/app/data")

STATIC_ROOT = _VAR_DIR / "static"
MEDIA_ROOT = _VAR_DIR / "media"
_LOG_PATH = _VAR_DIR / "proj.log"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': _VAR_DIR / f'{PROJECT_SLUG}.sqlite3',
    }
}

LOGGING['handlers']['file'] = {
    'level': 'INFO',
    'class': 'logging.FileHandler',
    'filename': _LOG_PATH,
    'formatter': 'verbose',
}
LOGGING['loggers']['proj']["handlers"] = ["file"]
