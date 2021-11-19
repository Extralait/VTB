from django.db import models
from django.utils.timezone import now


class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    kind = models.CharField(max_length=256)
    text = models.TextField()
    data = models.TextField()

    created_at = models.DateTimeField(default=now)
