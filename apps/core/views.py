"""All views from `core` app."""
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


# Create your views here.
@api_view()
def health_check(request: Request) -> Response:
    """`health_check` api_view.

    Returns `{'status_code': 200, 'detail': 'ok', 'result': 'working',}`
    in the response
    """
    return Response(
        {
            'status_code': 200,
            'detail': 'ok',
            'result': 'working',
        },
    )
