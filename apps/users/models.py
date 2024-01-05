"""`users` app models."""

from core.models import TimeStampedModel
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.managers import CustomUserManager


# Create your models here.
class User(TimeStampedModel, AbstractUser):
    """Custom `User` model.

    This custom `User` model does not have `username` field as default.
    The main field, that used for creating users - `email` field.
    """

    username: None = None
    email: models.EmailField = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD: str = 'email'  # noqa: WPS115
    REQUIRED_FIELDS: list[str] = []  # noqa: WPS115

    objects: CustomUserManager = CustomUserManager()  # noqa: WPS110

    def __str__(self) -> str:
        """`User` model instance string representation."""
        return self.email
