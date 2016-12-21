from __future__ import unicode_literals

from django.db import models
from model_utils import Choices


class Menu(models.Model):
    """Menu model for office foods."""

    CATEGORIES = Choices(
        'breakfast', 'Breakfast',
        'lunch', 'Lunch',
        'others', 'Others'
    )
    provided = models.DateField()
    food = models.CharField(max_length=1000)
    category = models.CharField(choices=CATEGORIES, max_length=20)
