# Generated by Django 3.0.5 on 2020-04-20 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_auto_20200420_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='islands',
            options={'ordering': ['ends']},
        ),
    ]