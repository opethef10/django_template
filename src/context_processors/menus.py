from src.menus import DEVELOPER_LINK, FOOTER_LINKS, SOCIAL_LINKS


def menus(request):
    return {
        'footer_links': FOOTER_LINKS,
        'social_links': SOCIAL_LINKS,
        'developer_link': DEVELOPER_LINK,
    }
