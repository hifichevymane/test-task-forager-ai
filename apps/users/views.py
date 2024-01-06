"""`users` app views."""

from django.db.models.query import QuerySet
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ListSerializer
from rest_framework.viewsets import GenericViewSet
from users.models import User
from users.permissions import IsAbleToEdit
from users.serializers import UserSerializer


# Create your views here.
class UserModelViewSet(  # noqa: WPS215
    GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
):
    """`User` model view set."""

    queryset: QuerySet[User] = User.objects.all()
    serializer_class: type[UserSerializer] = UserSerializer

    def get_permissions(self) -> None | list:
        """`get_permissions` method.

        If request method is `PUT` or `PATCH` method sets `self.permissions_classes`
        to `tuple` with `IsAbleToEdit` permission class.
        """
        if self.action in {'update', 'partial_update'}:
            self.permission_classes: tuple = (IsAbleToEdit, )

        return super().get_permissions()

    @action(detail=False, methods=('GET', ), url_path='unverified-users')
    def unverified_users(self, request: Request) -> Response:
        """`unverified_users`.

        Methods: `GET`.
        Returns `User` model instances where `is_active=False`
        """
        unverified_users: QuerySet[User] = User.objects.filter(is_active=False)

        serialized_unverified_users: ListSerializer = self.serializer_class(
            unverified_users, many=True,
        )

        return Response(serialized_unverified_users.data)
