# Generated by Django 3.2 on 2021-07-31 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablehost', '0012_alter_book_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(),
        ),
    ]