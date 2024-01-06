"""`storage` app serializers."""

from rest_framework import serializers


class StateSerializer(serializers.Serializer):
    """`StateSerializer`.

    JSON validation for `storage/` endpoint.
    """

    state: serializers.CharField = serializers.CharField(required=True)
