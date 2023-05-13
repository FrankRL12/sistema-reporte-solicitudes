from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Historial(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50)
    nombre_completo = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    mantenimiento = models.CharField(max_length=100, blank=True, null=True)
    tipo_equipo = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=50)
    class Meta:
        verbose_name='historial'
        verbose_name_plural='historiales'





class  Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Perfil de {self.user.username}'
    class Meta:
        verbose_name='perfil'
        verbose_name_plural='perfiles'


class Reporte(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50)
    nombre_completo = models.CharField(max_length=100)
    tipo_equipo = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=10, choices=(('En proceso', 'En proceso'), ('Finalizado', 'Finalizado')))
    timestamp=models.DateTimeField(default=timezone.now)
    historial = models.ForeignKey(Historial, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name='reporte'
        verbose_name_plural='reportes'

    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
        if not self.id:
            # Setea el id automáticamente si no se ha configurado.
            self.id = Reporte.objects.all().count() + 1
        super(Reporte, self).save(*args, **kwargs)


class Solicitud(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=50)
    nombre_completo = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    mantenimiento = models.CharField(max_length=100)
    estado = models.CharField(max_length=10, choices=(('En proceso', 'En proceso'), ('Finalizado', 'Finalizado')))
    timestamp=models.DateTimeField(default=timezone.now)
    historial = models.ForeignKey(Historial, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name='solicitud'
        verbose_name_plural='solicitudes'

    def __str__(self):
        return str(self.id)
    def save(self, *args, **kwargs):
        if not self.id:
            # Setea el id automáticamente si no se ha configurado.
            self.id = Solicitud.objects.all().count() + 1
        super(Solicitud, self).save(*args, **kwargs)

  


class Historial_Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    solicitudes = models.ManyToManyField(Solicitud)
    reportes = models.ManyToManyField(Reporte)

    class Meta:
        verbose_name='historial_usuarios'
        verbose_name_plural='historiales_usuarios'

