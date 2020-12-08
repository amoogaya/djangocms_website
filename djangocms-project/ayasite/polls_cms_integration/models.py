from cms.models import CMSPlugin
from django.db import models
from polls.models import Poll


# Create your models here.
class PollPluginModel(CMSPlugin):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.poll.question
