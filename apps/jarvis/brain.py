from __future__ import unicode_literals
import json
import re
import requests
from datetime import datetime
from datetime import timedelta

from django.contrib.auth import get_user_model

from food.mixins import FoodServiceMixins
from conversation.mixins import ConversationServiceMixin
from conversation.models import Question, Answer

from .utilities import clean_string

User = get_user_model()


class Jarvis(FoodServiceMixins, ConversationServiceMixin):
    """This is the official brain of Jarvis."""


    def __init__(self, request, *args, **kwargs):
        """Initialize jarvis."""
        commands = open('apps/jarvis/commands.json', 'r')
        self.commands = json.load(commands)
        self.request = request
        commands.close()

    def create_response(self):
        """Creates response."""
        request = self.request.data.get("text")  # slack message
        request = clean_string(request)
        handler, params = self.get_function(request)
        message, attachments = getattr(self, handler)(**params)
        print message, attachments
        response_url = self.request.data.get("response_url")
        response = JarvisResponse(message, response_url, attachments)
        response.send()

    def get_function(self, haystack):
        """Return the function from keywords."""
        commands = self.commands
        for command in commands:
            words = "|".join(commands[command].get("keywords"))
            requireds = "|".join(commands[command].get("requireds"))
            if re.search('({0})'.format(words), haystack) and \
                    re.search('({0})'.format(requireds), haystack):
                function_name = commands[command].get("function")
                function_params = commands[command].get("params", {})
                return function_name, function_params
        return "default_handler", {}


class JarvisResponse(object):
    """Jarvis response."""

    def __init__(self, message, url, attachments=[], *args, **kwargs):
        self.response = {
            'response_type': 'ephemeral',
            'text': message,
        }
        if attachments:
            self.response['attachments'] = attachments
        self.url = url

    def send(self):
        """Post response to url."""
        requests.post(url=self.url, data=json.dumps(self.response))
