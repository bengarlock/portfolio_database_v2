# Generated by Django 3.1.2 on 2021-04-02 11:34

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(max_length=20)),
                ('restaurant_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(blank=True, default='', max_length=50)),
                ('last_name', models.TextField(blank=True, default='', max_length=50)),
                ('phone_number', models.TextField(blank=True, default='')),
                ('guest_notes', models.TextField(blank=True, default='')),
                ('root_user', models.BooleanField(blank=True, default=False)),
                ('slot', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15), blank=True, default=list, size=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.TextField(default='two-top-horizontal')),
                ('position_left', models.TextField(default='0px')),
                ('position_top', models.TextField(default='0px')),
                ('name', models.TextField(blank=True)),
                ('restaurant_id', models.IntegerField(blank=True, default=1)),
                ('status', models.TextField(default='done')),
                ('reservation_id', models.IntegerField(blank=True, default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked', models.BooleanField(default=False)),
                ('time', models.TextField(default='5:00 PM')),
                ('party_size', models.IntegerField(default=0)),
                ('status', models.TextField(blank=True)),
                ('reservation_notes', models.TextField(blank=True)),
                ('tables', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15), blank=True, default=list, size=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='slots', to='tablehost.book')),
                ('guest', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='slots', to='tablehost.guest')),
            ],
        ),
    ]
