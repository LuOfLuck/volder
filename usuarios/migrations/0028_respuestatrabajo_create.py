# Generated by Django 2.2.3 on 2021-04-18 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0027_auto_20210417_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuestatrabajo',
            name='create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]