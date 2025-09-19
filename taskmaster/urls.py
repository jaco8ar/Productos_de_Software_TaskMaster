"""
URL configuration for taskmaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_usuario.views import notepad, usuario_pad, login_view, register_view
from app_objetivo.views import objetivo_view

from app_reporte.views import reporte_view
from app_tarea.views import tarea_view

from app_administrador.views import administrador_view
from app_recordatorio.views import recordatorio_view
from app_lista_de_tareas.views import lista_de_tareas_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', notepad, name='notepad'),
    path('usuario/', usuario_pad, name='usuario_pad'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('objetivos/', objetivo_view, name='objetivos'),
    path('reporte/', reporte_view, name='reporte'),
    path('tareas/', tarea_view, name='tareas'),
    path('administrador/', administrador_view, name='administrador'),
    path('recordatorio/', recordatorio_view, name='recordatorio'),
    path('lista_de_tareas/', lista_de_tareas_view, name='lista_de_tareas'),
]
