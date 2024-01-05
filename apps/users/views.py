"""`users` app views."""

from django.db.models.query import QuerySet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from users.models import User
from users.serializers import UserSerializer


# Create your views here.
class UserModelViewSet(  # noqa: WPS215
    GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
):
    """`User` model view set."""

    queryset: QuerySet[User] = User.objects.all()
    serializer_class: type[UserSerializer] = UserSerializer
