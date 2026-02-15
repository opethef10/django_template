from django.apps import apps
from django.contrib import admin

from .models import *
from src.utils import SelectRelatedModelAdmin


app_models = apps.get_app_config('example').get_models()
for model in app_models:
    admin.site.register(model)
