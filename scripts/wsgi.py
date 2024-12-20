import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'src.settings.production'

path = '/home/__PROJECT__/__PROJECT__.pythonanywhere.com'
if path not in sys.path:
    sys.path.insert(0, path)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
