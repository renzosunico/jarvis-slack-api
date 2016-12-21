from __future__ import unicode_literals

from django.conf import settings

from rest_framework import permissions



class SlackTokenPermission(permissions.BasePermission):
    """Check if request has token and match."""

    def has_permission(self, request, view):
        """Check token in request."""
        if request.method.upper() == "POST":
            token = request.data.get("token")
            if token not in settings.SLACK_TOKENS:
                return False
        return True
