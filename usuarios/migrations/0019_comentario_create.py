# Generated by Django 2.2.3 on 2021-01-21 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0018_comentario_trabajo'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
