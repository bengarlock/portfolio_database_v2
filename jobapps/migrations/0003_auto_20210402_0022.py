# Generated by Django 3.1.7 on 2021-04-02 00:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapps', '0002_auto_20210328_1151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapp',
            old_name='body',
            new_name='company_name',
        ),
        migrations.RenameField(
            model_name='jobapp',
            old_name='name',
            new_name='url',
        ),
        migrations.AddField(
            model_name='jobapp',
            name='contact',
            field=models.TextField(blank=True, default='Hiring Manager'),
        ),
        migrations.AddField(
            model_name='jobapp',
            name='job_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='jobapp',
            name='status',
            field=models.TextField(blank=True, default='Applied', max_length=50),
        ),
        migrations.AddField(
            model_name='jobapp',
            name='technologies',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, default=list, size=None),
        ),
    ]
