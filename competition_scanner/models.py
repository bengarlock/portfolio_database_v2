from django.db import models


# Create your models here.
class ResyRestaurant(models.Model):
    restaurant_name = models.CharField(max_length=3000, blank=True)
    resy_id = models.CharField(max_length=1000, blank=True)
    neighborhood = models.CharField(max_length=3000, blank=True)
    test = models.CharField(default="test", max_length=100)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class ResyTotalCount(models.Model):
    total_count = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class YelpRestaurant(models.Model):
    restaurant_name = models.CharField(max_length=3000, blank=True)
    yelp_id = models.CharField(max_length=1000, blank=True)
    neighborhood = models.CharField(max_length=3000, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class YelpTotals(models.Model):
    total_count = models.IntegerField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)