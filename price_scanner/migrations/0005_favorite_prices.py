# Generated by Django 3.1.7 on 2021-07-13 00:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_scanner', '0004_auto_20210712_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='prices',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15), blank=True, default=list, size=None),
        ),
    ]