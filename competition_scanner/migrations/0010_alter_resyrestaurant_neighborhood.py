# Generated by Django 3.2 on 2021-05-02 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition_scanner', '0009_alter_resyrestaurant_neighborhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resyrestaurant',
            name='neighborhood',
            field=models.CharField(blank=True, max_length=3000),
        ),
    ]
