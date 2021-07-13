from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Favorite(models.Model):
    name = models.CharField(max_length=3000, blank=True)
    url = models.CharField(max_length=3000, blank=True)
    image = models.CharField(max_length=3000, blank=True)
    test = models.CharField(max_length=3000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class Price(models.Model):
    price = models.CharField(max_length=3000, blank=True)
    favorite = models.ForeignKey(Favorite, related_name="prices", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
