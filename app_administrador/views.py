from django.shortcuts import render

def administrador_view(request):
	return render(request, 'administrador.html')
