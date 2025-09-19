

from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea

def tarea_view(request):
	if request.method == 'POST':
		# Check if this is a delete request
		if 'delete_tarea_id' in request.POST:
			tarea_id = request.POST.get('delete_tarea_id')
			tarea = get_object_or_404(Tarea, id=tarea_id)
			tarea.delete()
			return redirect('tareas')
		else:
			nombre = request.POST.get('nombre')
			descripcion = request.POST.get('descripcion')
			fecha_vencimiento = request.POST.get('fecha_vencimiento')
			if nombre and descripcion and fecha_vencimiento:
				Tarea.objects.create(
					nombre=nombre,
					descripcion=descripcion,
					fecha_vencimiento=fecha_vencimiento
				)
				return redirect('tareas')
	tareas = Tarea.objects.all().order_by('fecha_vencimiento')
	return render(request, 'tarea.html', {'tareas': tareas})
