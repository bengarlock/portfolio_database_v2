from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Jobapp(models.Model):
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=1000)
    owner = models.ForeignKey(User, related_name="jobapps", on_delete=models.CASCADE, null=True)
    technologies = ArrayField(models.CharField(max_length=255), default=list, blank=True)
    status = models.TextField(default="Applied", max_length=50, blank=True)
    contact = models.TextField(default="Hiring Manager", blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
