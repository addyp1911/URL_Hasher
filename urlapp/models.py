from __future__ import unicode_literals
from django.db import models

# Create your models here.


class URLs(models.Model):
    hashed_url = models.CharField(max_length=8, primary_key=True)
    target_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

