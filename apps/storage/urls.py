"""`storage` app urls."""

from django.urls import path
from django.urls.resolvers import URLPattern, URLResolver
from storage.views import StorageAPIView

urlpatterns: list[URLResolver | URLPattern] = [
    path('storage/', StorageAPIView.as_view(), name='storage'),
]
