# Generated by Django 3.1.7 on 2021-08-01 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_scanner', '0009_remove_favorite_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='price',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
