# Generated by Django 3.0.5 on 2020-04-24 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_skills'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skills',
            options={'ordering': ['skill_cost']},
        ),
    ]