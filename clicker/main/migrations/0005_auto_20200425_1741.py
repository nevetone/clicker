# Generated by Django 3.0.5 on 2020-04-25 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_cookies_var_o'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cookies',
            old_name='curret_gold',
            new_name='current_gold',
        ),
    ]
