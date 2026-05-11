from pathlib import Path

from .production import *


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
] + [m for m in MIDDLEWARE if m != 'django.middleware.security.SecurityMiddleware']

_VAR_DIR = Path("/data")
_VAR_DIR.mkdir(parents=True, exist_ok=True)

STATIC_ROOT = _VAR_DIR / "static"
MEDIA_ROOT = _VAR_DIR / "media"
_LOG_PATH = _VAR_DIR / "proj.log"

LOGGING['handlers']['file'] = {
    'level': 'INFO',
    'class': 'logging.FileHandler',
    'filename': _LOG_PATH,
    'formatter': 'verbose',
}
LOGGING['loggers']['proj']["handlers"] = ["file"]
