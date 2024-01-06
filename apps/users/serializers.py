"""`users` app serializers."""

from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """`User` model serialzier."""

    class Meta:  # noqa: WPS306,D106
        model: type[User] = User
        fields: str | tuple[str] = '__all__'

        extra_kwargs: dict[str, dict] = {
            'password': {'write_only': True},
        }
