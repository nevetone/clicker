# Generated by Django 3.0.5 on 2020-04-20 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20200420_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='islands',
            name='ends',
            field=models.IntegerField(default=1),
        ),
    ]