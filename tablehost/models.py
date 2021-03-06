from django.db import models
from django.contrib.postgres.fields import ArrayField


class Book(models.Model):
    date = models.DateField()
    restaurant_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class Guest(models.Model):
    first_name = models.TextField(default='', max_length=500, blank=True)
    last_name = models.TextField(default='', max_length=500, blank=True)
    phone_number = models.TextField(default='', blank=True)
    guest_notes = models.TextField(default='', blank=True)
    slot = ArrayField(models.CharField(max_length=15), default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=True)


class Restaurant(models.Model):
    name = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class Slot(models.Model):
    booked = models.BooleanField(default=False)
    time = models.TextField(default="5:00 PM")
    party_size = models.IntegerField(default=0)
    status = models.TextField(blank=True)
    reservation_notes = models.TextField(blank=True)
    tables = ArrayField(models.CharField(max_length=15), default=list, blank=True)
    book = models.ForeignKey(Book, related_name="slots", on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, related_name="guest", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class Table(models.Model):
    class_name = models.TextField(default="two-top-horizontal")
    position_left = models.TextField(default="0px")
    position_top = models.TextField(default="0px")
    name = models.TextField(blank=True)
    restaurant_id = models.IntegerField(default=1, blank=True)
    status = models.TextField(default='done')
    reservation_id = models.IntegerField(blank=True, default=1)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class Status(models.Model):
    color = models.CharField(default='#fff', max_length=1000)
    label = models.CharField(default='', max_length=1000)
    status_type = models.CharField(default='confirmation', max_length=1000)
    order = models.IntegerField(default=0)
