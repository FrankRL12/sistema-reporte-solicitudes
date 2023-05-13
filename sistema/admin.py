from django.contrib import admin
from .models import Reporte, Solicitud, Historial,Historial_Usuario, Perfil
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from datetime import date
import datetime



# Register your models here.
def mover_a_historial(modeladmin, request, queryset):
    for obj in queryset:
        historial = Historial.objects.create(
    cargo=obj.cargo,
    nombre_completo=obj.nombre_completo,
    ubicacion=obj.ubicacion,
    mantenimiento=obj.mantenimiento if isinstance(obj, Solicitud) else None,
    tipo_equipo=obj.tipo_equipo if isinstance(obj, Reporte) else None,
    descripcion=obj.descripcion if isinstance(obj, Reporte) else None,
    estado=obj.estado,
    usuario_id=request.user.id  # Agregar el valor del campo usuario_id
)
        if isinstance(obj, Solicitud):
            obj.historial = historial
        elif isinstance(obj, Reporte):
            obj.historial = historial
        obj.delete()
    modeladmin.message_user(request, "Objetos movidos al historial.")



def exportar_historial_a_pdf(modeladmin, request, queryset):
    # Definir la respuesta HTTP para descargar el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="historial.pdf"'

    # Definir el tamaño de página y crear el objeto SimpleDocTemplate
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Obtener los datos del queryset y crear la tabla
    data = []
    data.append(["Cargo", "Nombre completo", "Ubicación", "Mantenimiento", "Tipo de equipo", "Descripción", "Estado"])
    for obj in queryset:
        data.append([ obj.cargo, obj.nombre_completo, obj.ubicacion, obj.mantenimiento, obj.tipo_equipo, obj.descripcion, obj.estado])
    table = Table(data)

    # Aplicar estilos a la tabla
    styles = getSampleStyleSheet()
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)

    # Agregar la tabla al documento y generar el PDF
    elements = []
    elements.append(table)
    doc.build(elements)

    return response

exportar_historial_a_pdf.short_description = "Exportar historial a PDF"



class ReporteAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'nombre_completo', 'ubicacion', 'tipo_equipo', 'descripcion', 'estado', 'timestamp')
    list_editable = ('estado',)
    actions = [mover_a_historial]
    

class SolicitudAdmin(admin.ModelAdmin):
    list_display=('id', 'cargo', 'nombre_completo', 'ubicacion', 'mantenimiento', 'estado', 'timestamp')
    list_editable = ('estado',)
    actions = [mover_a_historial]

class HistorialAdmin(admin.ModelAdmin):
    list_display = ('id', 'cargo', 'nombre_completo', 'ubicacion', 'tipo_equipo', 'descripcion', 'mantenimiento', 'estado')
    actions = [exportar_historial_a_pdf]

admin.site.register(Reporte, ReporteAdmin)
admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Historial, HistorialAdmin)
admin.site.register(Historial_Usuario)
admin.site.register(Perfil)