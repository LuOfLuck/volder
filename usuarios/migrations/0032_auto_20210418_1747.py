# Generated by Django 2.2.3 on 2021-04-18 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0031_auto_20210418_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notatrabajo',
            name='respuestaTrabajo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.RespuestaTrabajo'),
        ),
    ]
