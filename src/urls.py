"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the 'include()' function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import HomeView, ContactView, SearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("accounts/", include("src.apps.accounts.urls")),
    path("contact/", ContactView.as_view(), name='contact'),
    path("pages/", include("django.contrib.flatpages.urls")),
    path("subscriptions/", include("src.apps.subscriptions.urls")),
    path('mdeditor/', include('mdeditor.urls')),
    path('docs/', include("src.apps.docs.urls")),
    path('api/search/', SearchView.as_view(), name='search'),
    path('', include('pwa.urls')),
    path('', HomeView.as_view(), name='home'),
    path("i18n/", include("django.conf.urls.i18n"))
]

if settings.DEBUG:
    urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
