from django.apps import apps
from django.conf import settings
from django.urls import include, path

from vuash.apps.core import views

urlpatterns = [
    path("", views.create_message, name="create_message"),
]

if settings.DEBUG:

    if apps.is_installed("debug_toolbar"):
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
