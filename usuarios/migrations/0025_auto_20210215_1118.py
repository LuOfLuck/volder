# Generated by Django 2.2.3 on 2021-02-15 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0024_auto_20210211_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_de_perfil/estudiante'),
        ),
        migrations.AddField(
            model_name='preceptor',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_de_perfil/preceptor'),
        ),
        migrations.AddField(
            model_name='profesor',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_de_perfil/profesor'),
        ),
        migrations.AddField(
            model_name='secretario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_de_perfil/secretario'),
        ),
    ]
