from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


# Create your views here.
@api_view()
def health_check(request: Request) -> Response:
    return Response(
        {
            'status_code': 200,
            'detail': 'ok',
            'result': 'working'
        }
    )