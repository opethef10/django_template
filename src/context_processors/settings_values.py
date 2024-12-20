from django.conf import settings


def project_settings(request):
    return {
        'PROJECT_SLUG': settings.PROJECT_SLUG,
        'PROJECT_NAME': settings.PROJECT_NAME,
        'PROJECT_DESCRIPTION': settings.PROJECT_DESCRIPTION,
        'PROJECT_DOMAIN': settings.PROJECT_DOMAIN,
        'PROJECT_URL': settings.PROJECT_URL,
    }
