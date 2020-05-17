from __future__ import unicode_literals
from django.utils import timezone
import pytz

from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    def __str__(self):
        return self.title
