from __future__ import unicode_literals
from django.db import models

# Create your models here.

class URLs(models.Model):
    hashed_url = models.CharField(max_length=8, primary_key=True)
    target_url = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    total_url_hits = models.IntegerField(default=0)
    hourly_hits = models.DecimalField(max_digits=8, decimal_places=3 ,default=0.0)

class URLHits(models.Model):
    url = models.ForeignKey(URLs, null=True, blank=True, on_delete=models.CASCADE, related_name="daily_hits")
    date = models.DateTimeField(auto_now_add=True)

