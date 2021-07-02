from django.db import models

class Day(models.Model):
    date = models.CharField(max_length=3000, blank=True)
    temp = models.IntegerField(default=0, blank=True)
    light = models.CharField(max_length=3000, default="sunny", blank=True)
    humidity = models.IntegerField(default=0, blank=True, null=True)
    rain = models.IntegerField(default=0, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
