# Generated by Django 3.0.5 on 2020-04-26 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200426_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userunits',
            name='cookies_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Cookies'),
        ),
        migrations.AlterField(
            model_name='userunits',
            name='unit_type',
            field=models.CharField(default='X', max_length=50),
        ),
    ]
