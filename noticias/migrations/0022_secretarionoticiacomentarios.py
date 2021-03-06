# Generated by Django 2.2.3 on 2021-03-05 02:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noticias', '0021_preceptornoticiacomentarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecretarioNoticiaComentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField(max_length=400)),
                ('noticia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='noticias.SecretarioNoticia')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Secretario Comenario',
                'verbose_name_plural': 'Secretarioes Comentarios',
            },
        ),
    ]
