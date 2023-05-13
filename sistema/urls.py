from django.urls import path
from sistema import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',LoginView.as_view(template_name='templates/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='templates/logout.html'), name='logout'),
    path('reportar/',login_required(views.reportar), name='reportar'),
    path('solicitar/',login_required(views.solicitar), name='solicitar'),
    path('inicio/',login_required(views.inicio), name='inicio'),
    path('historial_usuario/', login_required(views.historial_usuario), name='historial_usuario'),
]
