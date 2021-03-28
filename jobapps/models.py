from django.db import models
from django.contrib.auth.models import User

class Jobapp(models.Model):
    name = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name="jobapps", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
