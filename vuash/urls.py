from django.urls import path

from vuash.apps.core import views

urlpatterns = [
    path("", views.home, name="home"),
]
