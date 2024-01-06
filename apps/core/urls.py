"""`core` app urls."""

from core.views import health_check
from django.urls import include, path
from django.urls.resolvers import URLPattern, URLResolver

urlpatterns: list[URLResolver | URLPattern] = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', health_check, name='health_check'),
    path('', include('songs.urls')),
    path('', include('users.urls')),
    path('', include('storage.urls')),
]
