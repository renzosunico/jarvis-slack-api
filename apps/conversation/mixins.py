from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.postgres.search import TrigramSimilarity

from jarvis.utilities import clean_string

from .models import Question, Answer

User = get_user_model()

class ConversationServiceMixin(object):
    """Jarvis' conversation mechanism."""

    def default_handler(self, **kwargs):
        """Default handler."""
        user = self.request.user
        message = self.request.data.get("text")  # slack message
        message = clean_string(message)
        message = message.lower()

        if user.last_question and not user.last_question.answers.count():
            user.last_question.delete()

        questions = Question.objects.annotate(
            similarity=TrigramSimilarity('query', message)).filter(
                similarity__gte=0.9)
        if not questions:
            questions = Question.objects.create(
                query=clean_string(message.lower())
            )
            questions = Question.objects.filter(query=message)

        question = questions.first()
        answer = question.answers.first()

        if not answer:
            user.mode = User.MODES.ASKING
            user.last_question = question
            user.save()
            return "{0}, what should I say if they ask me \"{1}\"?".format(
                user.username, question.query), {
                "text": "Reply with keyword say. \
                    (e.g `/jarvis say Hello`)"
                }
        else:
            return answer.ans, {}

    def save_answer(self, **kwargs):
        """Save previous question's answer."""

        user = self.request.user
        if not user.last_question:
            return self.default_handler()

        ans = self.request.data.get("text")  # slack message
        ans = clean_string(ans)
        ans = ans[ans.find("say") + len("say"):]
        Answer.objects.create(question=user.last_question, ans=ans)

        user.last_question = None
        user.mode = User.MODES.ANSWERED
        user.save()

        return "Okay, {0}. {1}".format(user.username, ans), {}
