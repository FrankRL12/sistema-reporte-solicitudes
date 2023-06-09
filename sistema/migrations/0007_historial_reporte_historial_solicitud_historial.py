# Generated by Django 4.2 on 2023-05-07 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0006_alter_historial_usuario_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cargo', models.CharField(max_length=50)),
                ('nombre_completo', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=100)),
                ('mantenimiento', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_equipo', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('estado', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'historial',
                'verbose_name_plural': 'historiales',
            },
        ),
        migrations.AddField(
            model_name='reporte',
            name='historial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.historial'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='historial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.historial'),
        ),
    ]
