# Generated by Django 3.1.7 on 2021-04-12 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition_scanner', '0002_resytotalcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='YelpRestaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(blank=True, max_length=3000)),
                ('yelp_id', models.CharField(blank=True, max_length=1000)),
                ('neighborhood', models.CharField(blank=True, max_length=3000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='YelpTotals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_count', models.IntegerField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
