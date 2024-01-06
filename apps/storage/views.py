"""`storage` app views."""

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from storage.serializers import StateSerializer


# Create your views here.
class StorageAPIView(APIView):
    """`StorageAPIView`.

    This view is used to manipulate `state` variable with `GET` and `POST` requests.
    """

    state: str = 'Initial state'

    @classmethod
    def get_state(cls) -> str:  # noqa: WPS615
        """`get_state`.

        Returns current `state`.
        """
        return cls.state

    @classmethod
    def set_state(cls, new_state: str) -> None:  # noqa: WPS615
        """`set_state`.

        Set current `state` with new value.
        """
        cls.state = new_state

    def get(self, request: Request) -> Response:
        """`GET` method.

        Returns `state` variable.
        """
        return Response({'state': self.get_state()})

    def post(self, request: Request) -> Response:
        """`POST` method.

        Gets request data with `state` and change `state` variable.
        """
        serializer: StateSerializer = StateSerializer(data=request.data)

        if serializer.is_valid():
            validated_data: dict = serializer.validated_data
            self.set_state(validated_data['state'])

            return Response({'state': validated_data['state']})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
