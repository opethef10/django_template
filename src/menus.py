from django.utils.translation import gettext_lazy as _

NAVBAR_MENUS = [
    {
        "title": _("Docs"),
        "items": [
            {
                "label": _("Home"),
                "url_name": "docs:index",
                "args": [],
                "kwargs": {},
            },
            {
                "label": _("Setup"),
                "url_name": "docs:setup",
                "args": [],
                "kwargs": {},
            },
            {
                "label": _("Structure"),
                "url_name": "docs:structure",
                "args": [],
                "kwargs": {},
            },
            {
                "label": _("Settings"),
                "url_name": "docs:settings",
                "args": [],
                "kwargs": {},
            },
            {
                "label": _("Features"),
                "url_name": "docs:features",
                "args": [],
                "kwargs": {},
            },
            {
                "label": _("Deployment"),
                "url_name": "docs:deployment",
                "args": [],
                "kwargs": {},
            },
        ]
    },
]

FOOTER_LINKS = [
    {
        "label": _("Contact"),
        "url_name": "contact",
    },
    {
        "label": _("Documentation"),
        "url_name": "docs:index",
    },
    {
        "label": _("Setup Guide"),
        "url_name": "docs:setup",
    },
    {
        "label": _("Deployment"),
        "url_name": "docs:deployment",
    },
]

SOCIAL_LINKS = [

]
