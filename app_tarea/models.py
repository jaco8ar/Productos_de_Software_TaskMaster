from django.db import models

class Tarea(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField()
	fecha_vencimiento = models.DateField()

	def __str__(self):
		return self.nombre
