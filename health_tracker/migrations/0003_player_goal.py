# Generated by Django 3.2 on 2021-07-20 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_tracker', '0002_auto_20210719_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='goal',
            field=models.IntegerField(default=0),
        ),
    ]
