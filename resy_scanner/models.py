from django.db import models


# Create your models here.
class ResyRestaurant(models.Model):
    restaurant_name = models.CharField(max_length=3000, blank=True)
    resy_id = models.CharField(max_length=1000, blank=True)
    neighborhood = models.CharField(max_length=3000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
