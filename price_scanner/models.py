from django.db import models

# Create your models here.
class PriceUrls(models.Model):
    url = models.CharField(max_length=3000, blank=True)