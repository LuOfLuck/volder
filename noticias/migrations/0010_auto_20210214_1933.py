# Generated by Django 2.2.3 on 2021-02-14 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0009_auto_20210214_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secretarionoticia',
            name='preceptor',
            field=models.BooleanField(default=None),
        ),
    ]
