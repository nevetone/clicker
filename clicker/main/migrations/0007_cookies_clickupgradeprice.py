# Generated by Django 3.0.5 on 2020-04-25 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200425_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookies',
            name='clickUpgradePrice',
            field=models.FloatField(default=100),
        ),
    ]
