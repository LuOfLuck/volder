# Generated by Django 2.2.3 on 2021-02-14 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0010_auto_20210214_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secretarionoticia',
            name='preceptor',
        ),
    ]
