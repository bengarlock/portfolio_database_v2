# Generated by Django 3.2 on 2021-07-20 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_tracker', '0004_player_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
