from django.db import models
from django.utils import timezone

class Record(models.Model):
    phase = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    date = models.DateTimeField(
            blank=True, null=True)

