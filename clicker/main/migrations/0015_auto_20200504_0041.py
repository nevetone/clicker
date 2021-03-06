# Generated by Django 3.0.5 on 2020-05-03 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_cookies_visibleupgrades'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookies',
            name='current_mana',
            field=models.FloatField(default=100),
        ),
        migrations.AddField(
            model_name='cookies',
            name='current_passive_points',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='UserPassives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passive_id', models.CharField(default='X', max_length=50)),
                ('passive_count', models.FloatField(default=0)),
                ('passive_cost', models.FloatField(default=0)),
                ('cookies_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Cookies')),
            ],
        ),
    ]
