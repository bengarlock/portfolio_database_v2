# Generated by Django 3.2 on 2021-04-19 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition_scanner', '0006_resyrestaurant_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resyrestaurant',
            name='url',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]
