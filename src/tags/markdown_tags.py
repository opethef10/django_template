from django import template

register = template.Library()


@register.filter
def md_link(url):
    if not url:
        return url
    # Remove trailing slash if present
    if url.endswith('/'):
        url = url[:-1]
    # Add .md extension
    return url + '.md'
