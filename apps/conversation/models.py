from __future__ import unicode_literals

from django.db import models


class Question(models.Model):
    """Contains question details."""

    query = models.TextField()


class Answer(models.Model):
    """Answer to a question."""

    question = models.ForeignKey(Question, related_name="answers")
    ans = models.TextField()
