"""`users` app permissions.

Custom permission classes for `users` app views.
"""

from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import View
from users.models import User


class IsAbleToEdit(BasePermission):
    """`IsAbleToEdit` permission.

    Checks if user is able to edit the `User` instance.
    """

    def has_permission(self, request: Request, view: View) -> bool:
        """`has_permission` method.

        Checks if user is authenticated and returns `True` or `False`.
        """
        return request.user.is_authenticated

    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:  # noqa: WPS110
        """`has_object_permission` method.

        Checks if object pk equal current user pk. Returns `True` or `False`.
        """
        return obj.pk == request.user.pk
