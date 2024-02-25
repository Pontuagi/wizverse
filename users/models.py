from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class tweet(models.Model):
    text = models.TextField(max_length=300, default = '')
    datetime = models.DateTimeField(default = timezone.now)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    agreements = models.PositiveIntegerField(default=0)
    disagreements = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.text