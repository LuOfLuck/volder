# Generated by Django 2.2.3 on 2021-01-19 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volder_app', '0002_auto_20210118_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]
