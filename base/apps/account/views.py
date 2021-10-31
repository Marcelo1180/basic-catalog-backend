from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([IsAuthenticatedOrReadOnly])
def view_status(request):
    return Response({"status": "OK"}, status=status.HTTP_200_OK)
