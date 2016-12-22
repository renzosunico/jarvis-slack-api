from __future__ import unicode_literals
import re
from datetime import datetime
from datetime import timedelta

from core.utilities import local_time

from .models import Menu


class FoodServiceMixins(object):
    """Food service helper."""

    request = None

    def get_food(self, **kwargs):
        """Return food."""
        category = kwargs.get("category", {})
        category = Menu.CATEGORIES.breakfast if category == "breakfast" else \
            Menu.CATEGORIES.lunch
        data = kwargs.get("data", self.request.data)
        text = data.get("text")
        if re.search('(tomorrow|bukas)', text):
            food = Menu.objects.filter(
                provided=datetime.utcnow().date() + timedelta(days=1),
                category=category)
        elif re.search('(sa|on)', text) and re.search('\d+', text):
            digit = re.search('\d+', text)
            digit = int(digit.group(0))
            try:
                target = datetime.now().date().replace(day=digit)
                food = Menu.objects.filter(provided=target,
                    category=category)
            except ValueError:
                food = None
        else:
            food = Menu.objects.filter(
                provided=datetime.utcnow().date(),
                category=category)

        user = self.request.user.username
        message = food.first().food
        message = message if message else "There's no available food."
        message = "<@{0}>, {1}".format(user, message)
        return message, {}

    def get_relative_food(self, **kwargs):
        """Returns food depending on time."""
        now = local_time(datetime.now())
        breakfast_time = now.replace(hour=8, minute=30)
        lunch_time = now.replace(hour=12, minute=30)

        if now < breakfast_time:
            food = Menu.objects.filter(provided=now.date(),
                category=Menu.CATEGORIES.breakfast)
        elif now > breakfast_time and now < lunch_time:
            food = Menu.objects.filter(provided=now.date(),
                category=Menu.CATEGORIES.lunch)
        elif now > lunch_time:
            tomorrow = now + timedelta(days=1)
            food = Menu.objects.filter(provided=tomorrow.date(),
                category=Menu.CATEGORIES.breakfast)

        user = self.request.user.username
        message = food.first().food
        message = message if message else "There's no available food."
        message = "<@{0}>, {1}".format(user, message)
        return message, {}
