from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Reporte, Historial_Usuario, Solicitud, Historial

# Create your views here.


def inicio(request):
    historial_usuario = Historial_Usuario.objects.filter(usuario=request.user).first()
    solicitudes = []
    reportes = []
    if historial_usuario is not None:
        solicitudes = historial_usuario.solicitudes.all()
        reportes = Reporte.objects.filter(usuario=request.user)
        registros = list(solicitudes) + list(reportes)
    else:
        registros = []
    return render(request, 'templates/inicio.html', {'solicitudes': solicitudes, 'reportes': reportes})



def reportar(request):
    if request.method == 'POST':
        cargo = request.POST.get('cargo')
        nombre_completo = request.POST.get('nombre_completo')
        tipo_equipo= request.POST.get('tipo_equipo')
        ubicacion = request.POST.get('ubicacion')
        descripcion = request.POST.get('descripcion')
        estado = request.POST.get('estado', 'Enproceso')
        reporte = Reporte(usuario=request.user, cargo=cargo, nombre_completo=nombre_completo, tipo_equipo=tipo_equipo, ubicacion=ubicacion, descripcion=descripcion, estado=estado)
        reporte.save()

        historial, created = Historial_Usuario.objects.get_or_create(usuario=request.user)
        historial.reportes.add(reporte)
        historial.save()
        return redirect('inicio')

    return render(request, 'templates/reporte.html')




def solicitar(request):
    if request.method == 'POST':
        cargo = request.POST.get('cargo')
        nombre_completo = request.POST.get('nombre_completo')
        ubicacion = request.POST.get('ubicacion')
        mantenimiento = request.POST.get('mantenimiento')
        estado = request.POST.get('estado', 'Enproceso')
        
        # Obtener el siguiente id disponible para la solicitud
        
        solicitud = Solicitud(usuario=request.user, cargo=cargo, nombre_completo=nombre_completo, ubicacion=ubicacion, mantenimiento=mantenimiento, estado=estado)
        solicitud.save()
        
        historial, created = Historial_Usuario.objects.get_or_create(usuario=request.user)
        if historial is not None:
            historial.solicitudes.add(solicitud)
            historial.save()

        return redirect('inicio')

    return render(request, 'templates/solicitud.html')


def historial_usuario(request):
    # Obtener los datos del usuario actual
    usuario = request.user
    # Filtrar los registros de historial por el nombre de usuario
    historial = Historial.objects.filter(nombre_completo=usuario.username)
    # Pasar los registros al contexto de la plantilla
    contexto = {'historial': historial}
    # Renderizar la plantilla con el contexto
    return render(request, 'templates/historial.html', contexto)
