# Generated by Django 2.2.3 on 2021-01-19 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_tipodetarea'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipodetarea',
            old_name='Tipo',
            new_name='tipo',
        ),
    ]
