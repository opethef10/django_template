from django.urls import reverse
from django.contrib.sites.models import Site
from django.template import Template, Context
from django.utils.translation import gettext_lazy as _

TEMPLATE_STR = """
---
{{ topic_line }}

{{ link_line }}
{{ subscriptions_update_url }}
"""


def build_subscription_footer(topic_name: str) -> str:
    subscriptions_update_path = reverse('subscriptions:update')
    current_site = Site.objects.get_current()
    subscriptions_update_url = f"https://{current_site.domain}{subscriptions_update_path}"

    template = Template(TEMPLATE_STR)
    return template.render(
        Context({
            'topic_name': topic_name,
            'topic_line': _('You are receiving this email because you subscribed to the "%(topic_name)s" topic.') % {'topic_name': topic_name},
            'link_line': _("Click here to change your notification preferences:"),
            'subscriptions_update_url': subscriptions_update_url,
        })
    )
