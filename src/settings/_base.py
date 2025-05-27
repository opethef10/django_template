from pathlib import Path

from decouple import config, Csv
from django.contrib.messages import constants as messages
from django.utils.translation import gettext_lazy as _

PROJECT_DIR = Path(__file__).parent.parent
BASE_DIR = PROJECT_DIR.parent

PROJECT_SLUG = config("PROJECT_SLUG")
PROJECT_NAME = config("PROJECT_NAME")
PROJECT_DESCRIPTION = config("PROJECT_DESCRIPTION")
PROJECT_DOMAIN = config("PROJECT_DOMAIN")
PROJECT_ADMIN_NAME = config("PROJECT_ADMIN_NAME")
PROJECT_ADMIN_EMAIL = config("PROJECT_ADMIN_EMAIL")

PROJECT_URL = f"https://{PROJECT_DOMAIN}"
EMAIL_SUBJECT_PREFIX = f"[{PROJECT_NAME}] "

ROOT_URLCONF = 'src.urls'
INTERNAL_IPS = ["127.0.0.1"]
DEBUG = False

INSTALLED_APPS = [
    "django.contrib.flatpages",
    "allauth",
    "allauth.account",
    # "allauth.socialaccount",
    # "allauth.socialaccount.providers.facebook",
    # "allauth.socialaccount.providers.google",
    "allauth.usersessions",
    "src.apps.example",
    "django_minify_html",
    "django_extensions",
    "django.contrib.admin",
    'django.contrib.auth',
    'django.contrib.contenttypes',
    "django.contrib.humanize",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.redirects",
    "widget_tweaks",
    "pwa",
    "mobiledetect",
    "django_recaptcha",
    "mdeditor"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    "django_minify_html.middleware.MinifyHtmlMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
    'mobiledetect.middleware.DetectMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'src.context_processors.settings_values.project_settings',
                'src.context_processors.menus.menus',
            ],
            "libraries": {
                "form_tags": "src.tags.form_tags",
                "menu_tags": "src.tags.menu_tags",
            },
        },
    },
]


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# LOGGING
LOGGING = {
    'version': 1,
    # The version number of our log
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] (%(levelname)s) %(message)s",
            'datefmt': "%Y/%m/%d %H:%M:%S %z"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            'formatter': 'simple',
        },
    },
    'loggers': {
        'proj': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# Internationalization
LANGUAGE_CODE = "en"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = (
    ('en', _('English')),
)
LOCALE_PATHS = [
    PROJECT_DIR / 'locale/',
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [PROJECT_DIR / 'static']
MEDIA_URL = '/media/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

ADMINS = [
    (PROJECT_NAME, PROJECT_ADMIN_EMAIL),
]


MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# ==============================================================================
# FIRST-PARTY SETTINGS
# ==============================================================================

SITE_ID = 1

SECONDS = 1
MINUTES = 60 * SECONDS
HOURS = 60 * MINUTES

EMAIL_ENABLED = config("DJANGO_EMAIL_ENABLED", cast=bool, default=False)
RECAPTCHA_ENABLED = config("RECAPTCHA_ENABLED", cast=bool, default=True)

# ==============================================================================
# THIRD-PARTY SETTINGS
# ==============================================================================

X_FRAME_OPTIONS = 'SAMEORIGIN'

MDEDITOR_CONFIGS = {
    'default': {
        'width': '90% ',  # Custom edit box width
        'height': 500,  # Custom edit box height
        'toolbar': [
            "undo", "redo", "|",
            "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
            "h1", "h2", "h3", "h4", "h5", "h6", "|",
            "list-ul", "list-ol", "hr", "|",
            "link", "reference-link", "image", "code", "preformatted-text", "code-block",
            "table", "datetime", "emoji", "html-entities", "pagebreak", "goto-line", "|",
            "help", "info",
            "||", "preview", "watch", "fullscreen"
        ],  # custom edit box toolbar
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],
        'image_folder': 'editor',  # image save the folder name
        'theme': 'default',  # edit box theme, dark / default
        'preview_theme': 'default',  # Preview area theme, dark / default
        'editor_theme': 'default',  # edit area theme, pastel-on-dark / default
        'toolbar_autofixed': True,  # Whether the toolbar capitals
        'search_replace': True,  # Whether to open the search for replacement
        'emoji': True,  # whether to open the expression function
        'tex': True,  # whether to open the tex chart function
        'flow_chart': True,  # whether to open the flow chart function
        'sequence': True,  # Whether to open the sequence diagram function
        'watch': True,  # Live preview
        'lineWrapping': True,  # lineWrapping
        'lineNumbers': True,  # lineNumbers
        'language': 'en'  # zh / en / es
    }
}

# ==============================================================================
# ALLAUTH SETTINGS
# ==============================================================================
AUTHENTICATION_BACKENDS = ("allauth.account.auth_backends.AuthenticationBackend",)
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_CHANGE_EMAIL = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True

# ACCOUNT_LOGIN_BY_CODE_ENABLED = True
# ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = True

# MFA_SUPPORTED_TYPES = [
#     "webauthn",
#     "totp",
#     "recovery_codes",
# ]
# MFA_PASSKEY_LOGIN_ENABLED = True
# MFA_PASSKEY_SIGNUP_ENABLED = True

# SOCIALACCOUNT_AUTO_SIGNUP = False

# ==============================================================================
# PWA SETTINGS
# ==============================================================================
PWA_APP_NAME = PROJECT_NAME
PWA_APP_DESCRIPTION = PROJECT_DESCRIPTION
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/icons/android-chrome-192x192.png',
        'sizes': '160x160'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/icons/apple-touch-icon.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/icons/apple-touch-icon.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = LANGUAGE_CODE
PWA_SERVICE_WORKER_PATH = PROJECT_DIR / 'static' / 'js' / 'serviceworker.js'
