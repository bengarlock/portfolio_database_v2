# Generated by Django 3.2 on 2021-07-13 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('price_scanner', '0005_favorite_prices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='prices',
        ),
        migrations.AlterField(
            model_name='favorite',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='price',
            name='favorite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='price_scanner.favorite'),
        ),
        migrations.AlterField(
            model_name='price',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
