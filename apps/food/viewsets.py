from __future__ import unicode_literals
import json
from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions import SlackTokenPermission

from .models import Menu


class UploadMenuAPIView(APIView):
    """Endpoint for editing food menu."""

    permission_classes = (SlackTokenPermission, )

    def post(self, request, format=None):
        """Handles upload."""
        menus = request.data.get("menus", [])
        for menu in menus:
            menu, created = Menu.objects.get_or_create(
                category=menu.get('category'),
                food=menu.get("food"),
                provided=datetime.strptime(menu.get("provided"), "%Y/%m/%d"),
            )

        return Response({'success': True,
            'message': 'Records updated.'})
