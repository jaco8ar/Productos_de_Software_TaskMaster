from django.db import models
from app_usuario.models import Usuario

# Create your models here.
class Administrador(Usuario):
    permisos = models.CharField(max_length=150, default='todos')
    