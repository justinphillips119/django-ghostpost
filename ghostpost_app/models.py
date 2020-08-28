from django.db import models
from django.utils import timezone


class GhostpostModel(models.Model):
    post_choices = ((True, "Boast"), (False, "Roast"))
    post_type = models.BooleanField(choices=post_choices)
    content = models.CharField(max_length=280)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=timezone.now)

    @property
    def votes(self):
        return self.upvote - self.downvote

