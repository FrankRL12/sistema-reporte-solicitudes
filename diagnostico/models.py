from django.db import models

# Create your models here.
class Diagnostico(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    equipo = models.CharField(max_length=100)
    diagnostico = models.TextField()
    solucion = models.TextField()
    estado = models.CharField(max_length=20, choices=(('activo', 'activo'), ('en reparacion', 'en reparacion'), ('de vaja', 'de vaja')))
    class Meta:
        verbose_name='diagnostico'
        verbose_name_plural='diagnosticos'
