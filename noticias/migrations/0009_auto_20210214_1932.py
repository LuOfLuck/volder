# Generated by Django 2.2.3 on 2021-02-14 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0008_auto_20210214_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secretarionoticia',
            name='estudiante',
        ),
        migrations.RemoveField(
            model_name='secretarionoticia',
            name='profesores',
        ),
    ]
