# Generated by Django 2.2.3 on 2021-02-11 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_profesornoticia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secretarionoticia',
            name='mensaje',
            field=models.TextField(max_length=1999),
        ),
    ]
