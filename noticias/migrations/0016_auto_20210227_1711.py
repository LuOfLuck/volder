# Generated by Django 2.2.3 on 2021-02-27 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0015_auto_20210214_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secretarionoticia',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]