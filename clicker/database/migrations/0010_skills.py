# Generated by Django 3.0.5 on 2020-04-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_auto_20200420_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
                ('skill_id', models.IntegerField(default=0)),
                ('skill_cost', models.IntegerField(default=0)),
                ('skill_count', models.IntegerField(default=0)),
            ],
        ),
    ]
