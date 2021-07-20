from django.db import models


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=3000, default="", null=True, blank=True)
    status = models.IntegerField(default=0)
    goal = models.IntegerField(default=0)
