# Generated by Django 3.1.7 on 2021-06-18 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition_scanner', '0012_remove_yelprestaurant_neighborhood'),
    ]

    operations = [
        migrations.AddField(
            model_name='yelprestaurant',
            name='address',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]
