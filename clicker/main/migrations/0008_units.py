# Generated by Django 3.0.5 on 2020-04-26 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_cookies_clickupgradeprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookies_id', models.CharField(default='X', max_length=50)),
                ('unit_cost', models.FloatField(default=0)),
                ('unit_count', models.FloatField(default=0)),
            ],
        ),
    ]
