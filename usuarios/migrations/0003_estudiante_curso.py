# Generated by Django 2.2.3 on 2021-01-18 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('volder_app', '0002_auto_20210118_1937'),
        ('usuarios', '0002_auto_20210118_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='volder_app.Cursos'),
        ),
    ]
