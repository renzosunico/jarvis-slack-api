from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import exceptions
from rest_framework import authentication

from .models import SlackTeam
from .models import SlackChannel
User = get_user_model()


class SlackTokenAuthentication(authentication.BaseAuthentication):
    """Authenticator for slack webhook."""

    def authenticate(self, request):
        """Check for token."""
        try:
            token = request.POST.get("token")
            team_id = request.POST.get("team_id")
            team_domain = request.POST.get("team_domain")
            channel_id = request.POST.get("channel_id")
            channel_name = request.POST.get("channel_name")
            user_id = request.POST.get("user_id")
            username = request.POST.get("user_name")

            if token not in settings.SLACK_TOKENS:
                raise exceptions.AuthenticationFailed('Unauthorized Request')

            if not(token and team_id and team_domain and channel_id and
                    channel_name and user_id and username):
                raise exceptions.AuthenticationFailed('Deformed Request')

            # Get or Create Team
            team, t_created = SlackTeam.objects.get_or_create(
                id=team_id, defaults={'domain': team_domain}
            )

            # Get or Create Channel

            channel, c_created = SlackChannel.objects.get_or_create(
                id=channel_id, defaults={'name': channel_name, 'team': team}
            )

            # Get or Create User
            user, u_created = User.objects.get_or_create(
                id=user_id, defaults={'username': username, 'is_active': True}
            )

            # set team and channel in use object
            setattr(user, 'team', team)
            setattr(user, 'channel', team)

            return (user, None)
        except Exception as e:
            print e.message
