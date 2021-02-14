# Generated by Django 2.2.3 on 2021-02-11 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SecretarioNoticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=25)),
                ('mensaje', models.CharField(max_length=1999)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='noticias')),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Secretario Noticia',
                'verbose_name_plural': 'Secretario Noticias',
            },
        ),
    ]
