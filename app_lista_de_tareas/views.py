from django.shortcuts import render

def lista_de_tareas_view(request):
	return render(request, 'lista_de_tareas.html')
