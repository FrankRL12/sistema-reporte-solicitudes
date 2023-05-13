from django.contrib import admin
from .models import Diagnostico

# Register your models here.
class DiagnosticoAdmin(admin.ModelAdmin):
    list_display=('id', 'fecha', 'equipo', 'diagnostico', 'solucion', 'estado')
    list_editable = ('estado',)

admin.site.register(Diagnostico, DiagnosticoAdmin)
