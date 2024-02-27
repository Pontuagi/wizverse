from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class tweet(models.Model):
    # Tweet Model.
    text = models.TextField(max_length=300, default = '')
    datetime = models.DateTimeField(default = timezone.now)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    agreements = models.ManyToManyField(User, related_name='agreed_tweets', blank=True)
    disagreements = models.ManyToManyField(User, related_name='disagreed_tweets', blank=True)

    def __str__(self) -> str:
        return self.text