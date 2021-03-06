# Generated by Django 2.2.3 on 2021-02-14 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_auto_20210211_0433'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profesornoticia',
            options={'verbose_name': 'Profesor Noticia', 'verbose_name_plural': 'Profesores Noticias'},
        ),
        migrations.AddField(
            model_name='secretarionoticia',
            name='profesores',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profesornoticia',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='noticias/profesor'),
        ),
        migrations.AlterField(
            model_name='secretarionoticia',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='noticias/secretario'),
        ),
    ]
