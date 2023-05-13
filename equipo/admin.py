from django.contrib import admin
from .models import Equipo

# Register your models here.
class EquipoAdmin(admin.ModelAdmin):
    list_display=('id', 'tipo', 'marca', 'modelo', 'n_serie', 'n_inventario', 'estado')
    list_editable = ('estado',)
    search_fields = ('tipo', 'marca', 'modelo', 'n_serie', 'n_inventario')

admin.site.register(Equipo, EquipoAdmin)