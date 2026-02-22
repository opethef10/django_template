from urllib.parse import urlparse

from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag
def resolve_url(url_name, args=None, kwargs=None):
    """Resolves Django URL unless url_name is an absolute URI."""
    args = args or []
    kwargs = kwargs or {}

    if not url_name:
        return "#"

    if urlparse(url_name).netloc:
        return url_name

    try:
        return reverse(url_name, args=args, kwargs=kwargs)
    except NoReverseMatch:
        return "#"
