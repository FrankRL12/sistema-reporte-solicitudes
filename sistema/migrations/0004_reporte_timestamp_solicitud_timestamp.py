# Generated by Django 4.2 on 2023-05-06 23:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_alter_perfil_options_solicitud_reporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
