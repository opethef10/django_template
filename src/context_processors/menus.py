from src.menus import NAVBAR_MENUS, FOOTER_LINKS


def menus(request):
    return {
        'navbar_menus': NAVBAR_MENUS,
        'footer_links': FOOTER_LINKS,
    }
