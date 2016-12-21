from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """Override user model."""

    id = models.CharField(max_length=255, unique=True, primary_key=True)
    email = models.EmailField(_('email address'), unique=True, blank=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    username = models.CharField(max_length=255, unique=True)

    USERNAME_FIELD = 'username'


class SlackTeam(models.Model):
    """Representation of Slack Team."""

    id = models.CharField(max_length=255, unique=True, primary_key=True)
    domain = models.CharField(max_length=255, unique=True)


class SlackChannel(models.Model):
    """Representation of Channel."""

    id = models.CharField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    team = models.ForeignKey(SlackTeam, related_name="channels")
