# Generated by Django 2.2.3 on 2021-04-18 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0030_auto_20210418_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notatrabajo',
            name='comentario',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='notatrabajo',
            name='respuestaTrabajo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.RespuestaTrabajo'),
        ),
    ]
