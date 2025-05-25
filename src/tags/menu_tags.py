from urllib.parse import urlparse

from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()


def _is_absolute_url(url):
    """Check if the given string is an absolute URI (has a scheme)."""
    parsed = urlparse(url)
    return bool(parsed.scheme)


@register.simple_tag
def resolve_url(url_name, args=None, kwargs=None):
    """Resolves Django URL unless url_name is an absolute URI."""
    if not url_name:
        return "#"

    if _is_absolute_url(url_name):
        return url_name

    try:
        args = args or []
        kwargs = kwargs or {}
        return reverse(url_name, args=args, kwargs=kwargs)
    except NoReverseMatch:
        return "#"
