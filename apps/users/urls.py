"""`users` app urls."""

from django.urls import include, path
from django.urls.resolvers import URLPattern, URLResolver
from rest_framework.routers import SimpleRouter
from users.views import UserModelViewSet

router: SimpleRouter = SimpleRouter()
router.register('users', UserModelViewSet)

urlpatterns: list[URLResolver | URLPattern] = [
    path('', include(router.urls)),
]
