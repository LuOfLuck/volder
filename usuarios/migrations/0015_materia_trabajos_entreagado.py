# Generated by Django 2.2.3 on 2021-01-19 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0014_remove_trabajo_profesor'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='trabajos_entreagado',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
