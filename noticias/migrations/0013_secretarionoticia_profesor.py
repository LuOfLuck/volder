# Generated by Django 2.2.3 on 2021-02-14 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0012_secretarionoticia_preceptor'),
    ]

    operations = [
        migrations.AddField(
            model_name='secretarionoticia',
            name='profesor',
            field=models.BooleanField(default=None),
        ),
    ]
