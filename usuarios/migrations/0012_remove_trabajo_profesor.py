# Generated by Django 2.2.3 on 2021-01-19 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0011_trabajo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajo',
            name='profesor',
        ),
    ]
