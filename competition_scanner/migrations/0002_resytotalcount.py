# Generated by Django 3.1.7 on 2021-04-10 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition_scanner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResyTotalCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_count', models.IntegerField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]