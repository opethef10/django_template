from django.utils.translation import gettext_lazy as _

NAVBAR_MENUS = [
    {
        "title": _("Docs"),
        "items": [
            {
                "label": _("Home"),
                "url_name": "example:index",
                "args": [],
                "kwargs": {},
            },
            {
                "label": _("Setup"),
                "url_name": "example:setup",
                "args": [],
                "kwargs": {},
            },
            {
                "label": _("Structure"),
                "url_name": "example:structure",
                "args": [],
                "kwargs": {},
            },
            {
                "label": _("Settings"),
                "url_name": "example:settings",
                "args": [],
                "kwargs": {},
            },
            {
                "label": _("Features"),
                "url_name": "example:features",
                "args": [],
                "kwargs": {},
            },
            {
                "label": _("Deployment"),
                "url_name": "example:deployment",
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
        "url_name": "example:index",
    },
    {
        "label": _("Setup Guide"),
        "url_name": "example:setup",
    },
    {
        "label": _("PythonAnywhere"),
        "url_name": "example:pythonanywhere",
    },
]

SOCIAL_LINKS = [

]
