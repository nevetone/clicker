# Generated by Django 3.0.5 on 2020-04-27 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_userskills'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookies',
            name='visibleUpgrades',
            field=models.FloatField(default=-1),
        ),
    ]
