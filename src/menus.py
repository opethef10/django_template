from django.utils.translation import gettext_lazy as _

NAVBAR_MENUS = [

]

FOOTER_LINKS = [
    {
        "label": _("Contact"),
        "url_name": "contact",
    },
    {
        "label": _("Changelog"),
        "url_name": "django.contrib.flatpages.views.flatpage",
        "kwargs": {"url": "changelog/"},
    },
    {
        "label": _("Frequently Asked Questions"),
        "url_name": "django.contrib.flatpages.views.flatpage",
        "kwargs": {"url": "faq/"},
    },
]

SOCIAL_LINKS = [

]
