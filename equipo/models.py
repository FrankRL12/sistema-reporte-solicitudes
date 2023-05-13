from django.db import models

# Create your models here.
class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    n_serie = models.CharField(max_length=50)
    n_inventario = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, choices=(('activo', 'activo'), ('en reparacion', 'en reparacion'), ('de vaja', 'de vaja')))
    class Meta:
        verbose_name='equipo'
        verbose_name_plural='equipos'

    