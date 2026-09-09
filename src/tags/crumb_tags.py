from django import template
from django.apps import apps
from django.urls import reverse, NoReverseMatch

register = template.Library()


def _is_superuser(context):
    request = context.get("request")
    user = getattr(request, "user", None)
    return bool(user and user.is_superuser)


@register.simple_tag(takes_context=True)
def admin_edit_link(context, obj):
    if not _is_superuser(context) or obj is None:
        return ""
    opts = obj._meta
    url_name = f"admin:{opts.app_label}_{opts.model_name}_change"
    try:
        return reverse(url_name, args=[obj.pk])
    except NoReverseMatch:
        return ""


@register.simple_tag(takes_context=True)
def admin_changelist_link(context, target):
    if not _is_superuser(context) or target is None:
        return ""
    if isinstance(target, str):
        try:
            model = apps.get_model(target)
        except LookupError:
            return ""
        if model is None:
            return ""
    else:
        model = type(target)
    opts = model._meta
    url_name = f"admin:{opts.app_label}_{opts.model_name}_changelist"
    try:
        return reverse(url_name)
    except NoReverseMatch:
        return ""
