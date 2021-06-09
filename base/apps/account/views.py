import logging
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


logger = logging.getLogger(__name__)


@api_view(["GET"])
def view_status(request):
    logger.critical("Critical!")
    logger.error("Error!")
    logger.warning("Warning!")
    logger.info("Info OK")
    logger.debug("Debug OK")
    return Response({"status": "OK"}, status=status.HTTP_200_OK)
