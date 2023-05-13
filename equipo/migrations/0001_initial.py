# Generated by Django 4.2 on 2023-05-10 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('n_serie', models.CharField(max_length=50, unique=True)),
                ('n_inventario', models.CharField(max_length=50, unique=True)),
                ('estado', models.CharField(choices=[('activo', 'activo'), ('en reparacion', 'en reparacion'), ('de vaja', 'de vaja')], max_length=20)),
            ],
            options={
                'verbose_name': 'equipo',
                'verbose_name_plural': 'equipos',
            },
        ),
    ]
