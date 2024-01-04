# flake8: noqa: D100
from core.views import health_check
from django.urls import include, path

urlpatterns = [
    path("", health_check, name="health_check"),
    path("", include("songs.urls")),
]
