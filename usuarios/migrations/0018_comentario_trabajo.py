# Generated by Django 2.2.3 on 2021-01-21 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0017_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='trabajo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Trabajo'),
        ),
    ]