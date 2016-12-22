from __future__ import unicode_literals

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from jarvis.brain import Jarvis

from .authentications import SlackTokenAuthentication


class JarvisAPIView(APIView):
    """Jarvis main view. This is where all request will fall."""

    authentication_classes = (SlackTokenAuthentication,)

    def post(self, request, format=None):
        """Handles POST response of Jarvis."""
        jarvis = Jarvis(request=request)
        jarvis.create_response()
        return Response({'success': True, 'message': 'Request received.'})
