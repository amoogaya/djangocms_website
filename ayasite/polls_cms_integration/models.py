from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from polls.models import Poll


# Create your models here.
class PollPluginModel(CMSPlugin):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.poll.question


class MyModel(models.Model):
    title = models.CharField(null=True, max_length=200)
    description = models.TextField(null=True)
    my_placeholder = PlaceholderField('my_placeholder')
